import pytest
# from selenium.webdriver.common.by import By
from pages.authentication_page import RegisterPage
from constants.elements_path import ElementsPath
from utilities import auth_helper as auth
from utilities import helper as hp
import time
from pages.account_page import AccountPage

class TestAccount:
    @pytest.fixture
    def setup(self, driver):
        account_page = AccountPage(driver)
        account_page.redirect_self()
        return account_page

#### **Validation**
#first name invalid, another field is valid
    def test_first_name_invalid(self, setup):
        setup.clear_first_name()
        setup.enter_first_name("123")
        setup.click_save()
        hp.assert_text_in_message(setup, ElementsPath.ACCOUNT.ERROR, ElementsPath.ACCOUNT.FIRST_NAME.ERROR.INVALID)

#last name invalid, another field is valid
    def test_last_name_invalid(self, setup):
        setup.clear_last_name()
        setup.enter_last_name("123")
        setup.click_save()
        hp.assert_text_in_message(setup, ElementsPath.ACCOUNT.ERROR, ElementsPath.ACCOUNT.LAST_NAME.ERROR.INVALID)

#phone invalid, another field is valid
    def test_phone_invalid(self, setup):
        setup.clear_phone()
        setup.enter_phone("123")
        setup.click_save()
        hp.assert_text_in_message(setup, ElementsPath.ACCOUNT.ERROR, ElementsPath.ACCOUNT.PHONE.ERROR.INVALID)

#address invalid, another field is valid
    def test_address_invalid(self, setup):
        setup.clear_address()
        setup.enter_address("!" * 256)
        setup.click_save()
        hp.assert_text_in_message(setup, ElementsPath.ACCOUNT.ERROR, ElementsPath.ACCOUNT.ADDRESS.ERROR.MAX_LENGTH)

#city invalid, another field is valid
    def test_city_invalid(self, setup):
        setup.clear_city()
        setup.enter_city("!" * 101)
        setup.click_save()
        hp.assert_text_in_message(setup, ElementsPath.ACCOUNT.ERROR, ElementsPath.ACCOUNT.CITY.ERROR.MAX_LENGTH)

#postal code invalid, another field is valid
    def test_postal_code_invalid(self, setup):
        setup.clear_postal_code()
        setup.enter_postal_code("!" * 11)
        setup.click_save()
        hp.assert_text_in_message(setup, ElementsPath.ACCOUNT.ERROR, ElementsPath.ACCOUNT.POSTAL_CODE.ERROR.INVALID)

#first name max length, another field is valid
    def test_first_name_max_length(self, setup):
        setup.clear_first_name()
        setup.enter_first_name("a" * 101)
        setup.click_save()
        hp.assert_text_in_message(setup, ElementsPath.ACCOUNT.ERROR, ElementsPath.ACCOUNT.FIRST_NAME.ERROR.MAX_LENGTH)

#last name max length, another field is valid
    def test_last_name_max_length(self, setup):
        setup.clear_last_name()
        setup.enter_last_name("a" * 101)
        setup.click_save()
        hp.assert_text_in_message(setup, ElementsPath.ACCOUNT.ERROR, ElementsPath.ACCOUNT.LAST_NAME.ERROR.MAX_LENGTH)


#address max length, another field is valid
    def test_address_max_length(self, setup):
        setup.clear_address()
        setup.enter_address("a" * 256)
        setup.click_save()
        hp.assert_text_in_message(setup, ElementsPath.ACCOUNT.ERROR, ElementsPath.ACCOUNT.ADDRESS.ERROR.MAX_LENGTH)

#city max length, another field is valid
    def test_city_max_length(self, setup):
        setup.clear_city()
        setup.enter_city("a" * 101)
        setup.click_save()
        hp.assert_text_in_message(setup, ElementsPath.ACCOUNT.ERROR, ElementsPath.ACCOUNT.CITY.ERROR.MAX_LENGTH)

#postal code max length, another field is valid
    def test_postal_code_max_length(self, setup):
        setup.clear_postal_code()
        setup.enter_postal_code("1" * 11)
        setup.click_save()
        hp.assert_text_in_message(setup, ElementsPath.ACCOUNT.POSTAL_CODE.ERROR.PATH, ElementsPath.ACCOUNT.POSTAL_CODE.ERROR.INVALID)

#POSTAL_CODE min length, another field is valid
    def test_postal_code_min_length(self, setup):
        setup.clear_postal_code()
        setup.enter_postal_code("1")
        setup.click_save()
        hp.assert_text_in_message(setup, ElementsPath.ACCOUNT.ERROR, ElementsPath.ACCOUNT.POSTAL_CODE.ERROR.INVALID)

    def test_update_successfull(self, setup):
        setup.clear_first_name()
        setup.enter_first_name(auth.random_first_name())
        setup.click_save()
        hp.assert_alert_text_equals(setup.driver, ElementsPath.ACCOUNT.SUCCESS_TEXT)
#first name = null, another field is valid
    # def test_first_name_null(self, setup):
    #     setup.clear_first_name()
    #     time.sleep(1)
    #     setup.enter_first_name("")
    #     time.sleep(1)
    #     setup.click_save()
        
    #     time.sleep(5)
    #     hp.assert_alert_text_equals(setup.driver,ElementsPath.ACCOUNT.ERROR_REQUIRED_TEXT)

# #last name = null, another field is valid
#     def test_last_name_null(self, setup):
#         setup.clear_last_name()
#         setup.click_save()
#         hp.assert_alert_text_equals(setup.driver,ElementsPath.ACCOUNT.ERROR_REQUIRED_TEXT)

# #phone = null, another field is valid
#     def test_phone_null(self, setup):
#         setup.clear_phone()
#         setup.click_save()
#         hp.assert_alert_text_equals(setup.driver,ElementsPath.ACCOUNT.ERROR_REQUIRED_TEXT)



