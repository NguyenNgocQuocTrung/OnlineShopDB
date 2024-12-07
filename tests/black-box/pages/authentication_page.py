from constants.elements_path import ElementsPath

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.root = ElementsPath(driver)

    def redirect_self(self):
        self.root.click(ElementsPath.NAVIGATION.USER)

    def enter_email(self, email):
        self.root.input(ElementsPath.LOGIN.EMAIL.INPUT, email)

    def enter_password(self, password):
        self.root.input(ElementsPath.LOGIN.PASSWORD.INPUT, password)

    def click_login(self):
        self.root.click(ElementsPath.LOGIN.LOGIN_BUTTON)
    
    def click_redirect_register(self):
        self.root.click(ElementsPath.LOGIN.REDIRECT_REGISTER)

class RegisterPage:
    def __init__(self, driver):
        self.driver = driver
        self.root = ElementsPath(driver)
    
    def redirect_self(self):
        self.root.click(ElementsPath.NAVIGATION.USER)
        self.root.click(ElementsPath.LOGIN.REDIRECT_REGISTER)

    def get_error_fields(self):
        return self.root.elements(ElementsPath.REGISTER.CONDITION.ERROR_PATH_WITH_ATLEAST_1_ERROR)

    def get_error_messages(self, error_fields = None ):
        if error_fields is None:
            error_fields = self.get_error_fields()
        return [field.text for field in error_fields]

    def enter_first_name(self, first_name):
        self.root.input(ElementsPath.REGISTER.FIRST_NAME.INPUT, first_name)
    
    def enter_last_name(self, last_name):
        self.root.input(ElementsPath.REGISTER.LAST_NAME.INPUT, last_name)
    
    def enter_email(self, email):
        self.root.input(ElementsPath.REGISTER.EMAIL.INPUT, email)

    def enter_phone(self, phone):
        self.root.input(ElementsPath.REGISTER.PHONE.INPUT, phone)

    def enter_password(self, password):
        self.root.input(ElementsPath.REGISTER.PASSWORD.INPUT, password)

    def enter_address(self, address):
        self.root.input(ElementsPath.REGISTER.ADDRESS.INPUT, address)

    def enter_city(self, city):
        self.root.input(ElementsPath.REGISTER.CITY.INPUT, city)
    
    def enter_postal_code(self, postal_code):
        self.root.input(ElementsPath.REGISTER.POSTAL_CODE.INPUT, postal_code)
    
    def click_register(self):
        self.root.click(ElementsPath.REGISTER.REGISTER_BUTTON)
    
    def click_redirect_login(self):
        self.root.click(ElementsPath.REGISTER.REDIRECT_LOGIN)

    