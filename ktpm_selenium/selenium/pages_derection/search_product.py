import time
from selenium.webdriver.common.by import By


class SearchProducts:
    def __init__(self, driver):
        self.driver = driver

    def search_product(self, product_name):
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/nav/div[3]/div/input").send_keys(product_name)
        time.sleep(5)