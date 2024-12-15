import pytest
from selenium.webdriver.common.by import By
from pages.authentication_page import RegisterPage
from constants.elements_path import ElementsPath
from utilities import auth_helper as auth
from utilities import helper as hp
import time

class TestRegister:
    @pytest.fixture
    def setup(self, driver):
        register_page = RegisterPage(driver)
        register_page.redirect_self()
        return register_page

    # empty fields
    def test_register_with_empty_fields(self, setup):
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.LAST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.EMAIL.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PHONE.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PASSWORD.ERROR.REQUIRED_TEXT
        ]
        hp.assert_error_messsages_equals(setup, expected_message)

    # first name max length 101, all other fields are null
    def test_register_with_max_length_first_name_and_other_fields_null(self, setup):
        setup.enter_first_name(hp.random_string(101))
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.MAX_LENGTH,
            ElementsPath.REGISTER.LAST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.EMAIL.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PHONE.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PASSWORD.ERROR.REQUIRED_TEXT
        ]
        hp.assert_error_messsages_equals(setup, expected_message)

    # first name max length 101, all other fields are valid
    def test_register_with_max_length_first_name_and_other_fields_valid(self, setup):
        setup.enter_first_name(hp.random_string(101))  # invalid
        setup.enter_last_name(auth.random_last_name())
        setup.enter_email(auth.random_email())
        setup.enter_phone(auth.random_phone())
        setup.enter_password(auth.random_password())
        setup.enter_address(auth.random_address())
        setup.enter_city(auth.random_city())
        setup.enter_postal_code(auth.random_postal_code())
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.MAX_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)

    # last name max length 101, all other fields are null
    def test_register_with_max_length_last_name_and_other_fields_null(self, setup):
        setup.enter_last_name(hp.random_string(101))
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.LAST_NAME.ERROR.MAX_LENGTH,
            ElementsPath.REGISTER.EMAIL.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PHONE.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PASSWORD.ERROR.REQUIRED_TEXT
        ]
        hp.assert_error_messsages_equals(setup, expected_message)

    # last name max length 101, all other fields are valid
    def test_register_with_max_length_last_name_and_other_fields_valid(self, setup):
        setup.enter_first_name(auth.random_first_name())
        setup.enter_last_name(hp.random_string(101))  # invalid
        setup.enter_email(auth.random_email())
        setup.enter_phone(auth.random_phone())
        setup.enter_password(auth.random_password())
        setup.enter_address(auth.random_address())
        setup.enter_city(auth.random_city())
        setup.enter_postal_code(auth.random_postal_code())
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.LAST_NAME.ERROR.MAX_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)

    # email max length 256, all other fields are null
    def test_register_with_max_length_email_and_other_fields_null(self, setup):
        setup.enter_email(hp.random_string(256))
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.LAST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.EMAIL.ERROR.MAX_LENGTH,
            ElementsPath.REGISTER.PHONE.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PASSWORD.ERROR.REQUIRED_TEXT
        ]
        hp.assert_error_messsages_equals(setup, expected_message)

    # email max length 256, all other fields are valid
    def test_register_with_max_length_email_and_other_fields_valid(self, setup):
        setup.enter_first_name(auth.random_first_name())
        setup.enter_last_name(auth.random_last_name())
        setup.enter_email(hp.random_string(256))  # invalid
        setup.enter_phone(auth.random_phone())
        setup.enter_password(auth.random_password())
        setup.enter_address(auth.random_address())
        setup.enter_city(auth.random_city())
        setup.enter_postal_code(auth.random_postal_code())
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.EMAIL.ERROR.MAX_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # phone max length 12, all other fields are null
    def test_register_with_max_length_phone_and_other_fields_null(self, setup):
        setup.enter_phone(hp.random_digits_len(12))
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.LAST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.EMAIL.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PHONE.ERROR.MAX_LENGTH,
            ElementsPath.REGISTER.PASSWORD.ERROR.REQUIRED_TEXT
        ]
        hp.assert_error_messsages_equals(setup, expected_message)

    # phone max length 12, all other fields are valid
    def test_register_with_max_length_phone_and_other_fields_valid(self, setup):
        setup.enter_first_name(auth.random_first_name())
        setup.enter_last_name(auth.random_last_name())
        setup.enter_email(auth.random_email())
        setup.enter_phone(hp.random_digits_len(12))  # invalid
        setup.enter_password(auth.random_password())
        setup.enter_address(auth.random_address())
        setup.enter_city(auth.random_city())
        setup.enter_postal_code(auth.random_postal_code())
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.PHONE.ERROR.MAX_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # password max length 256, all other fields are null
    def test_register_with_max_length_password_and_other_fields_null(self, setup):
        setup.enter_password(hp.random_string(256))
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.LAST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.EMAIL.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PHONE.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PASSWORD.ERROR.MAX_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # password max length 256, all other fields are valid
    def test_register_with_max_length_password_and_other_fields_valid(self, setup):
        setup.enter_first_name(auth.random_first_name())
        setup.enter_last_name(auth.random_last_name())
        setup.enter_email(auth.random_email())
        setup.enter_phone(auth.random_phone())
        setup.enter_password(hp.random_string(256))  # invalid
        setup.enter_address(auth.random_address())
        setup.enter_city(auth.random_city())
        setup.enter_postal_code(auth.random_postal_code())
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.PASSWORD.ERROR.MAX_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # address max length 256, all other fields are null
    def test_register_with_max_length_address_and_other_fields_null(self, setup):
        setup.enter_address(hp.random_string(256))
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.LAST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.EMAIL.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PHONE.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PASSWORD.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.ADDRESS.ERROR.MAX_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # address max length 256, all other fields are valid
    def test_register_with_max_length_address_and_other_fields_valid(self, setup):
        setup.enter_first_name(auth.random_first_name())
        setup.enter_last_name(auth.random_last_name())
        setup.enter_email(auth.random_email())
        setup.enter_phone(auth.random_phone())
        setup.enter_password(auth.random_password())
        setup.enter_address(hp.random_string(256))  # invalid
        setup.enter_city(auth.random_city())
        setup.enter_postal_code(auth.random_postal_code())
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.ADDRESS.ERROR.MAX_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # city max length 101, all other fields are null
    def test_register_with_max_length_city_and_other_fields_null(self, setup):
        setup.enter_city(hp.random_string(101))
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.LAST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.EMAIL.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PHONE.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PASSWORD.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.CITY.ERROR.MAX_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # city max length 101, all other fields are valid
    def test_register_with_max_length_city_and_other_fields_valid(self, setup):
        setup.enter_first_name(auth.random_first_name())
        setup.enter_last_name(auth.random_last_name())
        setup.enter_email(auth.random_email())
        setup.enter_phone(auth.random_phone())
        setup.enter_password(auth.random_password())
        setup.enter_address(auth.random_address())
        setup.enter_city(hp.random_string(101))  # invalid
        setup.enter_postal_code(auth.random_postal_code())
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.CITY.ERROR.MAX_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # postal code max length 11, all other fields are null
    def test_register_with_max_length_postal_code_and_other_fields_null(self, setup):
        setup.enter_postal_code(hp.random_digits_len(11))
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.LAST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.EMAIL.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PHONE.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PASSWORD.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.POSTAL_CODE.ERROR.MAX_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # postal code max length 11, all other fields are valid
    def test_register_with_max_length_postal_code_and_other_fields_valid(self, setup):
        setup.enter_first_name(auth.random_first_name())
        setup.enter_last_name(auth.random_last_name())
        setup.enter_email(auth.random_email())
        setup.enter_phone(auth.random_phone())
        setup.enter_password(auth.random_password())
        setup.enter_address(auth.random_address())
        setup.enter_city(auth.random_city())
        setup.enter_postal_code(hp.random_digits_len(11))  # invalid
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.POSTAL_CODE.ERROR.MAX_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)

    # postal code min length 2, all other fields are null
    def test_register_with_min_length_postal_code_and_other_fields_null(self, setup):
        setup.enter_postal_code(hp.random_digits_len(2))
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.LAST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.EMAIL.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PHONE.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PASSWORD.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.POSTAL_CODE.ERROR.MIN_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)

    # postal code min length 2, all other fields are valid
    def test_register_with_min_length_postal_code_and_other_fields_valid(self, setup):
        setup.enter_first_name(auth.random_first_name())
        setup.enter_last_name(auth.random_last_name())
        setup.enter_email(auth.random_email())
        setup.enter_phone(auth.random_phone())
        setup.enter_password(auth.random_password())
        setup.enter_address(auth.random_address())
        setup.enter_city(auth.random_city())
        setup.enter_postal_code(hp.random_digits_len(2))  # invalid
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.POSTAL_CODE.ERROR.MIN_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)

    # first name invalid, all other fields are null
    def test_register_with_invalid_first_name_and_other_fields_null(self, setup):
        setup.enter_first_name(hp.random_digits_len(10))  # invalid
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.INVALID,
            ElementsPath.REGISTER.LAST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.EMAIL.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PHONE.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PASSWORD.ERROR.REQUIRED_TEXT
        ]
        hp.assert_error_messsages_equals(setup, expected_message)

    # first name invalid, all other fields are valid
    def test_register_with_invalid_first_name_and_other_fields_valid(self, setup):
        setup.enter_first_name(hp.random_digits_len(10))   # invalid
        setup.enter_last_name(auth.random_last_name())
        setup.enter_email(auth.random_email())
        setup.enter_phone(auth.random_phone())
        setup.enter_password(auth.random_password())
        setup.enter_address(auth.random_address())
        setup.enter_city(auth.random_city())
        setup.enter_postal_code(auth.random_postal_code())
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.INVALID
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # last name invalid, all other fields are null
    def test_register_with_invalid_last_name_and_other_fields_null(self, setup):
        setup.enter_last_name(hp.random_digits_len(10)) 
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.LAST_NAME.ERROR.INVALID,
            ElementsPath.REGISTER.EMAIL.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PHONE.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PASSWORD.ERROR.REQUIRED_TEXT
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # last name invalid, all other fields are valid
    def test_register_with_invalid_last_name_and_other_fields_valid(self, setup):
        setup.enter_first_name(auth.random_first_name())
        setup.enter_last_name(hp.random_digits_len(10))   # invalid
        setup.enter_email(auth.random_email())
        setup.enter_phone(auth.random_phone())
        setup.enter_password(auth.random_password())
        setup.enter_address(auth.random_address())
        setup.enter_city(auth.random_city())
        setup.enter_postal_code(auth.random_postal_code())
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.LAST_NAME.ERROR.INVALID
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # email invalid, all other fields are null
    def test_register_with_invalid_email_and_other_fields_null(self, setup):
        setup.enter_email(hp.random_string(101))
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.LAST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.EMAIL.ERROR.INVALID,
            ElementsPath.REGISTER.PHONE.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PASSWORD.ERROR.REQUIRED_TEXT
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # email invalid, all other fields are valid
    def test_register_with_invalid_email_and_other_fields_valid(self, setup):
        setup.enter_first_name(auth.random_first_name())
        setup.enter_last_name(auth.random_last_name())
        setup.enter_email(hp.random_string(101))  # invalid
        setup.enter_phone(auth.random_phone())
        setup.enter_password(auth.random_password())
        setup.enter_address(auth.random_address())
        setup.enter_city(auth.random_city())
        setup.enter_postal_code(auth.random_postal_code())
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.EMAIL.ERROR.INVALID
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # phone invalid, all other fields are null
    def test_register_with_invalid_phone_and_other_fields_null(self, setup):
        setup.enter_phone("1" +hp.random_string(10))
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.LAST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.EMAIL.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PHONE.ERROR.INVALID,
            ElementsPath.REGISTER.PASSWORD.ERROR.REQUIRED_TEXT
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # phone invalid, all other fields are valid
    def test_register_with_invalid_phone_and_other_fields_valid(self, setup):
        setup.enter_first_name(auth.random_first_name())
        setup.enter_last_name(auth.random_last_name())
        setup.enter_email(auth.random_email())
        setup.enter_phone("1" +hp.random_string(10))  # invalid
        setup.enter_password(auth.random_password())
        setup.enter_address(auth.random_address())
        setup.enter_city(auth.random_city())
        setup.enter_postal_code(auth.random_postal_code())
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.PHONE.ERROR.INVALID
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # password invalid, all other fields are null
    def test_register_with_invalid_password_and_other_fields_null(self, setup):
        setup.enter_password(hp.random_string(9))
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.LAST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.EMAIL.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PHONE.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PASSWORD.ERROR.INVALID
        ]
        hp.assert_error_messsages_equals(setup, expected_message)

    # password invalid, all other fields are valid
    def test_register_with_invalid_password_and_other_fields_valid(self, setup):
        setup.enter_first_name(auth.random_first_name())
        setup.enter_last_name(auth.random_last_name())
        setup.enter_email(auth.random_email())
        setup.enter_phone(auth.random_phone())
        setup.enter_password(hp.random_string(9))  # invalid
        setup.enter_address(auth.random_address())
        setup.enter_city(auth.random_city())
        setup.enter_postal_code(auth.random_postal_code())
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.PASSWORD.ERROR.INVALID
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # password min length 7, all other fields are null
    def test_register_with_min_length_password_and_other_fields_null(self, setup):
        setup.enter_password(hp.random_string(7))
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.LAST_NAME.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.EMAIL.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PHONE.ERROR.REQUIRED_TEXT,
            ElementsPath.REGISTER.PASSWORD.ERROR.MIN_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # password min length 7, all other fields are valid
    def test_register_with_min_length_password_and_other_fields_valid(self, setup):
        setup.enter_first_name(auth.random_first_name())
        setup.enter_last_name(auth.random_last_name())
        setup.enter_email(auth.random_email())
        setup.enter_phone(auth.random_phone())
        setup.enter_password(hp.random_string(7))
        setup.enter_address(auth.random_address())
        setup.enter_city(auth.random_city())
        setup.enter_postal_code(auth.random_postal_code())
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.PASSWORD.ERROR.MIN_LENGTH
        ]
        hp.assert_error_messsages_equals(setup, expected_message)
    
    # all field max length
    def test_register_with_max_length_fields(self, setup):
        setup.enter_first_name(hp.random_string(101))
        setup.enter_last_name(hp.random_string(101))
        setup.enter_email(hp.random_string(256))
        setup.enter_phone(hp.random_digits_len(12))
        setup.enter_password(hp.random_string(256))
        setup.enter_address(hp.random_string(256))
        setup.enter_city(hp.random_string(101))
        setup.enter_postal_code(hp.random_digits_len(6)+"$")
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.MAX_LENGTH,
            ElementsPath.REGISTER.LAST_NAME.ERROR.MAX_LENGTH,
            ElementsPath.REGISTER.EMAIL.ERROR.MAX_LENGTH,
            ElementsPath.REGISTER.PHONE.ERROR.MAX_LENGTH,
            ElementsPath.REGISTER.PASSWORD.ERROR.MAX_LENGTH,
            ElementsPath.REGISTER.ADDRESS.ERROR.MAX_LENGTH,
            ElementsPath.REGISTER.CITY.ERROR.MAX_LENGTH,
            ElementsPath.REGISTER.POSTAL_CODE.ERROR.INVALID
        ]
        hp.assert_error_messsages_equals(setup, expected_message)

    # first name invalid, last_name invalid, email invalid, phone invalid, password invalid, postal code invalid
    def test_register_with_invalid_fields(self, setup):
        setup.enter_first_name(hp.random_string_with_space(99) + "$")
        setup.enter_last_name(hp.random_string_with_space(99) + "$")
        setup.enter_email(hp.random_string(100))
        setup.enter_phone(hp.random_string(10))
        setup.enter_password(hp.random_string(9))
        setup.enter_postal_code(hp.random_string_and_digits(6) + "$")
        setup.click_register()
        expected_message = [
            ElementsPath.REGISTER.FIRST_NAME.ERROR.INVALID,
            ElementsPath.REGISTER.LAST_NAME.ERROR.INVALID,
            ElementsPath.REGISTER.EMAIL.ERROR.INVALID,
            ElementsPath.REGISTER.PHONE.ERROR.INVALID,
            ElementsPath.REGISTER.PASSWORD.ERROR.INVALID,
            ElementsPath.REGISTER.POSTAL_CODE.ERROR.INVALID
        ]
        hp.assert_error_messsages_equals(setup, expected_message)

    # register successfully
    def test_register_random_information_successfully(self, setup):
        setup.enter_first_name(auth.random_first_name())
        setup.enter_last_name(auth.random_last_name())
        setup.enter_email(auth.random_email())
        setup.enter_phone(auth.random_phone())
        setup.enter_password(auth.random_password())
        setup.enter_address(auth.random_address())
        setup.enter_city(auth.random_city())
        setup.enter_postal_code(auth.random_postal_code())
        setup.click_register()
        hp.assert_alert_text_equals(setup.driver, ElementsPath.REGISTER.REGISTER_SUCCESS_TEXT)
        hp.assert_text_in_src_page(setup.driver,"Login")

#================================================================================