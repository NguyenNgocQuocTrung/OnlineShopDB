from constants.elements_path import ElementsPath
from pages.authentication_page import LoginPage
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class AccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.login = LoginPage(driver)
        self.root = ElementsPath(driver)
    
    def redirect_self(self):
        self.login.redirect_self()
        self.login.enter_email(ElementsPath.ACCOUNT.DATA.EMAIL)
        self.login.enter_password(ElementsPath.ACCOUNT.DATA.PASSWORD)
        self.login.click_login()
        alert = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        alert.accept()
        time.sleep(0.1)

    def get_text(self, path):
        return self.root.text(path)

    def get_error_fields(self):
        return self.root.elements(ElementsPath.ACCOUNT.CONDITION.ERROR_PATH_WITH_ATLEAST_1_ERROR)

    def get_error_messages(self, error_fields=None):
        if error_fields is None:
            error_fields = self.get_error_fields()
        return [field.text for field in error_fields]
    
    def enter_first_name(self, first_name):
        self.root.input(ElementsPath.ACCOUNT.FIRST_NAME.INPUT, first_name)
    
    def enter_last_name(self, last_name):
        self.root.input(ElementsPath.ACCOUNT.LAST_NAME.INPUT, last_name)
    
    def enter_phone(self, phone):
        self.root.input(ElementsPath.ACCOUNT.PHONE.INPUT, phone)

    def enter_address(self, address):
        self.root.input(ElementsPath.ACCOUNT.ADDRESS.INPUT, address)

    def enter_city(self, city):
        self.root.input(ElementsPath.ACCOUNT.CITY.INPUT, city)
    
    def enter_postal_code(self, postal_code):
        self.root.input(ElementsPath.ACCOUNT.POSTAL_CODE.INPUT, postal_code)
    
    def click_save(self):
        self.root.click(ElementsPath.ACCOUNT.SAVE_BUTTON)
    
    def click_cancel(self):
        self.root.click(ElementsPath.ACCOUNT.CANCEL_BUTTON)
    def clear_first_name(self):
        self.root.clear(ElementsPath.ACCOUNT.FIRST_NAME.INPUT)
    def clear_last_name(self):
        self.root.clear(ElementsPath.ACCOUNT.LAST_NAME.INPUT)
    def clear_phone(self):
        self.root.clear(ElementsPath.ACCOUNT.PHONE.INPUT)
    def clear_address(self):
        self.root.clear(ElementsPath.ACCOUNT.ADDRESS.INPUT)
    def clear_city(self):
        self.root.clear(ElementsPath.ACCOUNT.CITY.INPUT)
    def clear_postal_code(self):
        self.root.clear(ElementsPath.ACCOUNT.POSTAL_CODE.INPUT)
    


        



