import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ElementsPath:
    class NAVIGATION:
        SHOP = "//*[@id=\"root\"]/nav/div[2]/ul/li[1]/a"
        CONTACT_US = "//*[@id=\"root\"]/nav/div[2]/ul/li[2]/a"
        ABOUT_US = "//*[@id=\"root\"]/nav/div[2]/ul/li[3]/a"
        USER = '//*[@id=\"root\"]/nav/div[2]/div/a[1]'
        WISHLIST = "//*[@id='root']/nav/div[2]/div/a[2]/div/svg/path"
        CART = "//*[@id='root']/nav/div[2]/div/a[3]/div"
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
                PATH = "" 
                REQUIRED_TEXT = "First name is required"
                MAX_LENGTH = "Must be at most 100 characters"
                INVALID = "Only characters and spaces are allowed"
            INPUT = "//*[@id=\"root\"]/div[1]/div[1]/div/form/label[1]/div/input"

        class LAST_NAME:
            class ERROR:
                PATH = "" 
                REQUIRED_TEXT = "Last name is required"
                MAX_LENGTH = "Must be at most 100 characters"
                INVALID = "Only characters and spaces are allowed"
            INPUT = "//*[@id=\"root\"]/div[1]/div[1]/div/form/label[2]/div/input"

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
    
    class ACCOUNT:
        class DATA:
            EMAIL = 'elroydevops@gmail.com'
            PASSWORD = "0900000009"
        class FIRST_NAME:
            class ERROR:
                PATH = '//*[@id="root"]/div[1]/div/div[1]/div/label[1]/span'
                REQUIRED_TEXT = "First name is required"
                MAX_LENGTH = "Must be at most 100 characters"
                INVALID = "Only characters and spaces are allowed"
            INPUT = '//*[@id="root"]/div[1]/div/div[1]/div/label[1]/input'

        class LAST_NAME:
            class ERROR:
                PATH = '//*[@id="root"]/div[1]/div/div[1]/div/label[2]/span'
                REQUIRED_TEXT = "Last name is required"
                MAX_LENGTH = "Must be at most 100 characters"
                INVALID = "Only characters and spaces are allowed"
            INPUT = '//*[@id="root"]/div[1]/div/div[1]/div/label[2]/input'
        ERROR = "//*[@class='error-text'][1]"

        # class EMAIL:

        #     class ERROR:
        #         PATH = '//*[@id="root"]/div[1]/div/div[1]/div/label[3]/span'
        #         REQUIRED_TEXT = "Email is required"
        #         MAX_LENGTH = "Must be at most 255 characters"
        #         INVALID = "Invalid email address"
        #     INPUT = '//*[@id="root"]/div[1]/div/div[1]/div/label[3]/input'

        class PHONE:
            class ERROR:
                PATH = '//*[@id="root"]/div[1]/div/div[1]/label[2]/span '
                REQUIRED_TEXT = "Phone number is required"
                MAX_LENGTH = "Must be at most 11 characters"
                INVALID = "Phone number must start with 0 and contain 10-11 digits"
            INPUT = '//*[@id="root"]/div[1]/div/div[1]/label[2]/input'

        class ADDRESS:
            class ERROR:
                PATH = '//*[@id="root"]/div[1]/div/div[1]/div/label[5]/span'
                MAX_LENGTH = "Must be at most 255 characters"
            INPUT = '//*[@id="root"]/div[1]/div/label/input'

        class CITY:
            class ERROR:
                PATH = '//*[@id="root"]/div[1]/div/div[1]/div/label[6]/span'
                MAX_LENGTH = "Must be at most 100 characters"
            INPUT = '//*[@id="root"]/div[1]/div/div[2]/label[2]/input'

        class POSTAL_CODE:
            class ERROR:
                PATH = '//*[@id="root"]/div[1]/div/div[2]/label[1]/span'
                MIN_LENGTH = "Must be at least 3 characters"
                MAX_LENGTH = "Must be at most 10 characters"
                INVALID = "Invalid postal code. Only letters, numbers, and spaces are allowed."
            INPUT = '//*[@id="root"]/div[1]/div/div[2]/label[1]/input'
        SUCCESS_TEXT = "Update successful"
        ERROR_REQUIRED_TEXT = "First name, last name, and phone number are required"
        SAVE_BUTTON = '//*[@id="root"]/div[1]/div/div[3]/button[2]'
        CANCEL_BUTTON = '//*[@id="root"]/div[1]/div/div[3]/button[1]'

    class MINI_CART:
        NO_ITEM = "//*[@id='root']/nav/div[2]/div/a[3]/div/span"

    class SHOP:
        class ITEMS:
            class ITEM:
                class SIZES:
                    SIZES = "//*[@id='size-select']//option"
                
                SIZES_SELECTOR = "//select[@id='size-select']"
                NAME = "//*[@id='root']/div[1]/div[2]/h1"
                ADD_TO_BASKET = "//*[@id='root']/div[1]/div[2]/div[2]/button[1]"
            
            ITEMS_PATH = "//*[@id='root']/div[1]/div[2]//div"
                
        class BUTTONS:
            NEXT_BUTTON = "//*[@id='root']/div[1]/div[3]/button[2]"
            PREVIOUS_BUTTON = "//*[@id='root']/div[1]/div[3]/button[2]"
    
    class CART:
        class CART_ITEMS:
            TITLE = "//*[@id='root']/div[1]/div[1]/h1"
            ITEM_LIST = "//*[@id='root']/div[1]/div[1]/div"
            CLEAR_CART = "//*[@id='root']/div[1]/div[1]/div/a"

            class ITEM:
                REMOVE = "//*[@id='root']/div[1]/div[1]/div/div[1]/div/div[1]/a[2]"
                NAME = "//div[@class='cart-item-left']//a/p"
                PRICE = "//div[@class='cart-item-right']/p"
                QUANTITY = "//*[@id='root']/div[1]/div[1]/div/div/div/div[2]/div/input"
                DECREASE = "//div[@class='cart-item']//div[@class='cart-item-quantity']/a[1]"
                INCREASE = "//div[@class='cart-item']//div[@class='cart-item-quantity']/a[2]"
            

        class DISCOUNT:
            DISCOUNT_INPUT = "//div[@class='discount-code']/input"
            APPLY_BUTTON = "//div[@class='discount-code']/button"
        
        class SUMMARY:
            SUBTOTAL = "//*[@id='root']/div[1]/div[2]/div/div[1]/p[2]"
            DISCOUNT = "//*[@id='root']/div[1]/div[2]/div/div[2]/p[2]"
            TOTAL    = "//*[@id='root']/div[1]/div[2]/div/div[5]/p[2]"
            CHECKOUT = "//*[@id='root']/div[1]/div[2]/div[1]/a/button"
              
        class IS_EMPTY:
            TEXT_PATH = "//*[@id='root']/div[1]/div/p"
            TEXT = "There’s nothing in your bag yet."

        

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
    
    def clear(self, path):
        self.sleep()
        self.element(path).clear()
        self.sleep()

    def select_by_visible_text(self, path, name):
        select = Select(self.element(path))
        select.select_by_visible_text(name)

    def select_by_value(self, path, value):
        select = Select(self.element(path))
        select.select_by_value(value)
    
    def select_by_index(self, path, value):
        select = Select(self.element(path))
        select.select_by_index(value)
        
    def click(self, path):
        self.sleep()
        self.element(path).click()
        self.sleep()

    def click_from_elements(self, path, element_no = 1):
        self.sleep()
        self.element(f'{path}{[element_no]}').click()
        self.sleep()

    def input(self, path, keys):
        self.sleep()
        self.element(path).send_keys(keys)
        self.sleep()