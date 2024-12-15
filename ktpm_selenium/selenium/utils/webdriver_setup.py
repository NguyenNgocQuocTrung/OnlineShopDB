import pytest
from selenium import webdriver


class Driver:
    @pytest.fixture(scope="function", autouse=True)
    def driver(self):
        """Set up Chrome WebDriver with custom options."""
        options = webdriver.EdgeOptions()
        options.add_argument("--disable-blink-features=AutofillSaveCard")  # Tắt lưu thẻ
        options.add_argument("--disable-features=AutofillSaveCard")  # Tắt Autofill cho thẻ
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,  # Vô hiệu hóa popup lưu mật khẩu
            "profile.password_manager_enabled": False,  # Vô hiệu hóa trình quản lý mật khẩu
            "autofill.profile_enabled": False,  # Vô hiệu hóa tự động điền thông tin
            "autofill.credit_card_enabled": False  # Vô hiệu hóa lưu thẻ tín dụng
        })
        driver = webdriver.Edge(options=options)
        driver.maximize_window()
        yield driver
        driver.quit()
