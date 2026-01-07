#pytest -m smoke //tagging
#pytest -n 10 // pytest-xdist plugin you need to run in parallel.

import os
import json
import pytest
from PageObjects.login import LoginPage
from PageObjects.shopPage import ShopPage

# =========================================================
# STEP 1: Build absolute path to test data JSON file
# =========================================================

# Get the directory of the current test file
current_dir = os.path.dirname(os.path.abspath(__file__))

# Navigate up to project root and then into the 'data' folder
# (Assuming your structure is PyTestDemo/pytestsDemo/test_file.py)
test_data_path = os.path.normpath(os.path.join(current_dir, "..", "data", "test_e2eTestFramework.json"))

# =========================================================
# STEP 2: Load test data from JSON file
# =========================================================

with open(test_data_path, "r") as file:
    test_data = json.load(file)
    test_list = test_data["data"]

# =========================================================
# STEP 3: Data-driven test using pytest parametrization
# =========================================================

@pytest.mark.smoke
@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    """
    End-to-End test:
    1. Login
    2. Add product to cart
    3. Checkout and validate order
    """

    # Get browser instance from pytest fixture
    driver = browserInstance

    # Open application URL
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.maximize_window()

    # =====================================================
    # STEP 4: Login Page actions
    # =====================================================
    login_page = LoginPage(driver)
    print(login_page.getTitle())
    login_page.login(
        test_list_item["userEmail"],
        test_list_item["userPassword"]
    )

    # =====================================================
    # STEP 5: Shop Page actions
    # =====================================================
    shop_page = ShopPage(driver)
    print(login_page.getTitle())
    shop_page.add_product_to_cart(
        test_list_item["productName"]
    )

    # =====================================================
    # STEP 6: Checkout & Order Confirmation
    # =====================================================
    checkout_confirmation = shop_page.goToCart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("India")
    checkout_confirmation.validate_order()