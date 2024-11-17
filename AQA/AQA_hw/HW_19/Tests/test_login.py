import pytest
from selenium.webdriver.common.by import By


@pytest.mark.parametrize("username, password, expected_url", [
    ("admin", "admin", "https://demo.applitools.com/app.html")
])

def test_login(browser, username, password, expected_url):
    browser.get("https://demo.applitools.com/")

    # Find elements
    username_field = browser.find_element(By.ID, "username")
    password_field = browser.find_element(By.ID, "password")
    login_button = browser.find_element(By.ID, "log-in")

    # Interact with elements
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()


    # Checking results
    assert expected_url == browser.current_url, f"Error {username}/{password}"
