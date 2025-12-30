import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action = "store", default = "chrome", help="browser selection"
    )


@pytest.fixture(scope = "function")
def browserInstance(request):
    browser_name = request.config.getoption("browser_name") #setting opitons for the command line, which browser to launch
    if browser_name == "chrome" :
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
        driver.implicitly_wait(5)
    yield driver #befor test function execution.

    driver.close() #post test function execution.