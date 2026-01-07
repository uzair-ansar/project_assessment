import pytest
from pages.login_page import LoginPage

@pytest.mark.failure
def test_failed_login(driver):
    login = LoginPage(driver)
    login.open()
    login.login("locked_out_user", "secret_sauce")
    assert "locked out" in login.get_error_message().lower()