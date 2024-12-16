
import time
from selenium.webdriver.common.by import By


class FilterElementsPath:
    class FILTER:
        FILTER_BOX = "//*[@id=\"root\"]/div[1]/div[1]/div[1]/a"
        SIZE_BOX = "//*[@id=\"size\"]"
        MIN_PRICE = "//*[@id=\"minPrice\"]"
        MAX_PRICE = "//*[@id=\"maxPrice\"]"
        PRICE_TEXT = "//*[@id=\"root\"]/div[1]/div[2]/div[1]/div[2]/a/p[2]"
        OPTION = "option"
        VALUE = "value"
        SORT = "//*[@id=\"sort\"]"
        SORT_BY_LOWEST_TO_HIGHEST = "//*[@id=\"sort\"]/option[2]"
        SORT_BY_HIGHEST_TO_LOWEST = "//*[@id=\"sort\"]/option[3]"
        PRODUCT = "//*[@id=\"root\"]/div[1]/div[2]/div[1]"
        PRODUCT_SIZE_BOX = "//*[@id=\"size-select\"]"
        PRODUCT_CARD = "//*[@class='product-card']"
        PRODUCT_PRICE = ".//div[@class='product-info']/p"

    class ERROR:
        NO_RESULTS = "//*[@class='filter-no-results-message']"


    def __init__(self, driver):
            self.driver = driver
            
    def sleep(self, seconds = 0.1):
            time.sleep(seconds)

    def element(self, path):
            return self.driver.find_element(By.XPATH, path)
        
    def elements(self, path):
            return self.driver.find_elements(By.XPATH, path)
    
    def elements_name(self,path):
            return self.driver.find_elements(By.TAG_NAME, path)

    def text(self, path):
            return self.element(path).text
        
    def click(self, path):
            self.sleep(seconds=1)
            self.element(path).click()
            self.sleep(seconds=1)

    def input(self, path, keys):
            self.sleep()
            self.element(path).send_keys(keys)
            self.sleep()