import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(params=["chrome"])
def browser(request):
    browser_type = request.param
    if browser_type == "chrome":
        options = ChromeOptions()
        driver = webdriver.Chrome(service=ChromeService(), options=options)
    else:
        raise ValueError(f"Unknown browser: {browser_type}")

    driver.implicitly_wait(10)
    yield driver
    driver.quit()