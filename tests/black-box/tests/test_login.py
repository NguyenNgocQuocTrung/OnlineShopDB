import pytest

from constants.elements_path import ElementsPath
from utilities import helper as hp
from ktpm_selenium.selenium.pages_derection.home_page import HomePage
from ktpm_selenium.selenium.pages_derection.login_page import LoginPage

class TestLogin:
    @pytest.fixture
    def setup(self,driver):
        login_page = LoginPage(driver)
        login_page.redirect_self()
        return login_page
#email= null. password= null
    def test_login_with_empty_fields(self,setup):
        setup.click_login()
        assert setup.root.text(ElementsPath.LOGIN.EMAIL.ERROR.PATH) == ElementsPath.LOGIN.EMAIL.ERROR.REQUIRED_TEXT
        assert setup.root.text(ElementsPath.LOGIN.PASSWORD.ERROR.PATH) == ElementsPath.LOGIN.PASSWORD.ERROR.REQUIRED_TEXT

#email= invalid. password= null
    def test_login_with_invalid_email(self,setup):
        setup.enter_email("invalid_email")
        setup.click_login()
        assert setup.root.text(ElementsPath.LOGIN.EMAIL.ERROR.PATH) == ElementsPath.LOGIN.EMAIL.ERROR.INVALID_TEXT
        assert setup.root.text(ElementsPath.LOGIN.PASSWORD.ERROR.PATH) == ElementsPath.LOGIN.PASSWORD.ERROR.REQUIRED_TEXT

#email= valid. password= null
    def test_login_with_valid_email_and_empty_password(self,setup):
        setup.enter_email("valid_user@gmail.com")
        setup.click_login()
        assert setup.root.text(ElementsPath.LOGIN.CONDITION.ERROR_PATH_WITH_ATLEAST_1_ERROR) == ElementsPath.LOGIN.PASSWORD.ERROR.REQUIRED_TEXT

#email= valid. password= invalid
    def test_login_with_valid_email_and_invalid_password(self,setup):
        setup.enter_email("valid_user@gmail.com")
        setup.enter_password("123")
        setup.click_login()
        assert setup.root.text(ElementsPath.LOGIN.CONDITION.ERROR_PATH_WITH_ATLEAST_1_ERROR) == ElementsPath.LOGIN.PASSWORD.ERROR.INVALID

#email= null. password= valid
    def test_login_with_empty_email_and_valid_password(self, setup):
        setup.enter_password("valid_password")
        setup.click_login()
        assert setup.root.text(ElementsPath.LOGIN.EMAIL.ERROR.PATH) == ElementsPath.LOGIN.EMAIL.ERROR.REQUIRED_TEXT

#email= valid. password= valid, not registered
    def test_login_with_valid_email_and_password(self,setup):
        setup.enter_email("valid_user@gmail.com")
        setup.enter_password("valid_password")
        setup.click_login()
        hp.assert_alert_text_equals(setup.driver,"Invalid email or password")
#email=valid. password=valid, registered
    def test_login_with_valid_email_and_password_registered(self,setup):
        setup.enter_email("elroydevops@gmail.com")
        setup.enter_password("0900000009")
        setup.click_login()
        hp.assert_current_url_equals_account_url(setup.driver)

#================================================================================

    def test_login_valid_info(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.go_to_home_page()
        email = "elroydevops@gmail.com"
        password = "0900000009"
        login_page.go_to_login(email, password)