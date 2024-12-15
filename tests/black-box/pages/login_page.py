import time
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    # Navigate to the login page
    def go_to_login(self, email, password):
        """Natvigate to the login page."""
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div/nav/div[2]/div/a[1]/div").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/form/label[1]/div/input").send_keys(email)
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/form/label[2]/div/input").send_keys(
            password)
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/div/form/button").click()
        time.sleep(5)

    # click on logout
    def logout(self):
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/a/span").click()
        self.driver.find_element(By.XPATH, "/html/body/nav/div/div[2]/ul/li[2]/div/ul/li[5]/a").click()
        time.sleep(5)

    # get error message
    def get_error_message(self):
        return self.driver.find_element(By.XPATH, "/html/body/div").text
