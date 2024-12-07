import time
from selenium.webdriver.common.by import By

class ElementsPath:
    class NAVIGATION:
        SHOP = "//*[@id=\"root\"]/nav/div[2]/ul/li[1]/a"
        CONTACT_US = "//*[@id=\"root\"]/nav/div[2]/ul/li[2]/a"
        ABOUT_US = "//*[@id=\"root\"]/nav/div[2]/ul/li[3]/a"
        USER = '//*[@id=\"root\"]/nav/div[2]/div/a[1]'
        WISHLIST = "//*[@id='root']/nav/div[2]/div/a[2]/div/svg/path"
        CART = "//*[@id='root']/nav/div[2]/div/a[3]/div/svg/path"
        INDEX = "//*[@id='root']/nav/div[2]/a"
    
    class LOGIN:

        class EMAIL:
            class ERROR:
                PATH = "//*[@id=\"root\"]/div[1]/div[1]/div/form/span[1]"
                REQUIRED_TEXT = "Email is required"
                INVALID_TEXT = "Invalid email address"
            INPUT = "//*[@id=\"root\"]/div[1]/div[1]/div/form/label[1]/div/input"

        class PASSWORD:
            class ERROR:
                PATH = "//*[@id=\"root\"]/div[1]/div[1]/div/form/span[2]"
                MIN_LENGTH = "Password must be at least 8 characters long"
                REQUIRED_TEXT = "Password is required"
                INVALID = "Password must be at least 8 characters long"
            INPUT = "//*[@id=\"root\"]/div[1]/div[1]/div/form/label[2]/div/input"

        class CONDITION:
            ERROR_PATH_WITH_ATLEAST_1_ERROR ="//*[@id=\"root\"]/div[1]/div[1]/div/form/span" #example: email valid, password invalid

        class ERROR:
            PATH = "//*[@class='error-message']"
            INVALID_TEXT = "Invalid email or password"

        LOGIN_BUTTON = "//*[@id='root']/div[1]/div[1]/div/form/button"
        REDIRECT_REGISTER = "//*[@id='root']/div[1]/div[2]/a[2]"
    
    class REGISTER:
        class FIRST_NAME:
            class ERROR:
                PATH = ""  # Đường dẫn XPath hoặc CSS Selector cho trường First Name
                REQUIRED_TEXT = "First name is required"
                MAX_LENGTH = "Must be at most 100 characters"
                INVALID = "Only characters and spaces are allowed"
            INPUT = "//*[@id=\"root\"]/div[1]/div[1]/div/form/label[1]/div/input"
        class LAST_NAME:
            class ERROR:
                PATH = ""  # Đường dẫn XPath hoặc CSS Selector cho trường Last Name
                REQUIRED_TEXT = "Last name is required"
                MAX_LENGTH = "Must be at most 100 characters"
                INVALID = "Only characters and spaces are allowed"
            INPUT = "//*[@id=\"root\"]/div[1]/div[1]/div/form/label[2]/div/input"
        class EMAIL:
            class ERROR:
                REQUIRED_TEXT = "Email is required"
                MAX_LENGTH = "Must be at most 255 characters"
                INVALID = "Invalid email address"
            INPUT = "//*[@id='root']/div[1]/div[1]/div/form/label[3]/div/input"
        class PHONE:
            class ERROR:
                REQUIRED_TEXT = "Phone number is required"
                MAX_LENGTH = "Must be at most 11 characters"
                INVALID = "Phone number must start with 0 and contain 10-11 digits"
            INPUT = "//*[@id='root']/div[1]/div[1]/div/form/label[4]/div/input"
        class PASSWORD:
            class ERROR:
                REQUIRED_TEXT = "Password is required"
                MAX_LENGTH = "Must be at most 255 characters"
                MIN_LENGTH = "Must be at least 8 characters"
                INVALID = "Must contain uppercase, lowercase, number, and special character"
            INPUT = "//*[@id='root']/div[1]/div[1]/div/form/label[5]/div/input"
        class ADDRESS:
            class ERROR:
                MAX_LENGTH = "Must be at most 255 characters"
            INPUT = "//*[@id='root']/div[1]/div[1]/div/form/label[6]/div/input"
        class CITY:
            class ERROR:
                PATH = "" 
                MAX_LENGTH = "Must be at most 100 characters"
            INPUT = "//*[@id='root']/div[1]/div[1]/div/form/label[7]/div/input"
        class POSTAL_CODE:
            class ERROR:
                PATH = ""
                MIN_LENGTH = "Must be at least 3 characters"
                MAX_LENGTH = "Must be at most 10 characters"
                INVALID = "Invalid postal code. Only letters, numbers, and spaces are allowed."
            INPUT = "//*[@id='root']/div[1]/div[1]/div/form/label[8]/div/input"
        
        class CONDITION:
            ERROR_PATH_WITH_ATLEAST_1_ERROR = "//*[@id='root']/div[1]/div[1]/div/form/span"  #example: 1 field valid
        REGISTER_SUCCESS_TEXT = "Registration successfully"
        REGISTER_BUTTON = "//*[@id='root']/div[1]/div[1]/div/form/button"
        REDIRECT_LOGIN = "//*[@id='root']/div[1]/div[2]/a[1]"
    
    
        

    def __init__(self, driver):
        self.driver = driver
        
    def sleep(self, seconds = 0.1):
        time.sleep(seconds)

    def element(self, path):
        return self.driver.find_element(By.XPATH, path)
    
    def elements(self, path):
        return self.driver.find_elements(By.XPATH, path)

    def text(self, path):
        return self.element(path).text
    
    def click(self, path):
        self.sleep()
        self.element(path).click()
        self.sleep()

    def input(self, path, keys):
        self.sleep()
        self.element(path).send_keys(keys)
        self.sleep()
