import pytest
import os
from selenium import webdriver
from datetime import datetime
from pytest_html import extras


# ---------------- Browser Option ----------------
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="firefox",
        help="browser selection"
    )


# ---------------- Browser Fixture ----------------
@pytest.fixture(scope="function")
def browserInstance(request):
    browser_name = request.config.getoption("--browser_name").lower()

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.implicitly_wait(5)
    yield driver
    driver.quit()


# ---------------- Screenshot Hook ----------------
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    # Ignore expected failures
    xfail = hasattr(report, "wasxfail")

    # Capture screenshot on failure
    if report.when in ("setup", "call") and report.failed and not xfail:

        driver = item.funcargs.get("browserInstance")
        if driver is None:
            print("❌ Driver not available — screenshot skipped")
            return

        # Screenshot directory
        reports_dir = r"C:\Users\tpss\PycharmProjects\Testing-Python\PyTest\reports"
        os.makedirs(reports_dir, exist_ok=True)

        # Screenshot file name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        safe_test_name = item.nodeid.replace("::", "_").replace("/", "_")
        screenshot_path = os.path.join(
            reports_dir, f"{safe_test_name}_{timestamp}.png"
        )

        # Take screenshot
        if driver.save_screenshot(screenshot_path):
            print(f"📸 Screenshot saved: {screenshot_path}")
        else:
            print("❌ Screenshot capture failed")
            return

        # Attach screenshot to pytest-html report
        if hasattr(report, "extra"):
            report.extra.append(extras.image(screenshot_path))
        else:
            report.extra = [extras.image(screenshot_path)]
