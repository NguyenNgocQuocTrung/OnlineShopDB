import time
from selenium.webdriver.common.by import By


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_shopping_cart(self):
        self.driver.find_element(By.XPATH, "/html/body/div/nav/div[2]/div/a[3]/div").click()
        time.sleep(5)

    def go_to_checkout(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[1]/a/button").click()
        time.sleep(5)
