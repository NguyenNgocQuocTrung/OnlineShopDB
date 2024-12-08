from ktpm_selenium.selenium.pages_derection.home_page import HomePage
from ktpm_selenium.selenium.pages_derection.login_page import LoginPage

class TestLogin:
    def test_login_valid_info(self, driver):
        home_page = HomePage(driver)
        login_page = LoginPage(driver)

        home_page.go_to_home_page()
        email = "elroydevops@gmail.com"
        password = "0900000009"
        login_page.go_to_login(email, password)