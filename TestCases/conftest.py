import pytest
from selenium import webdriver
from selenium.webdriver.safari.service import Service


@pytest.fixture(scope="function")
def setup():
    """Fixture to initialize Safari WebDriver and return the driver instance."""
    service = Service("/usr/bin/safaridriver")
    driver = webdriver.Safari(service=service)
    driver.maximize_window()

    yield driver  # Provide the driver to the test


def pytest_addoption(parser):
    parser.addoption("--browser")  # This will get the value from CLI /hooks


@pytest.fixture
def browser(request):  # This will return the Browser value to setup method
    return request.configgetoption("--browser")
