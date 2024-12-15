import time
from selenium.webdriver.common.by import By

class ProductPage():
    def __init__(self, driver):
        self.driver = driver

    def go_to_product_page(self):
        self.driver.find_element(By.XPATH, "/html/body/div/nav/div[2]/ul/li[1]/a").click()
        time.sleep(3)