import pytest
from pages.login_page import LoginPage

@pytest.mark.success
def test_successful_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("standard_user", "secret_sauce")
    assert login.is_logo_present()