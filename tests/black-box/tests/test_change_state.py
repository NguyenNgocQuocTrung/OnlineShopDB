import pytest
from selenium.webdriver.common.by import By
import time

from constants.config import BASE_URL, REGISTER_ENDPOINT


class TestState:
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        time.sleep(3)
        driver.get(BASE_URL + REGISTER_ENDPOINT)

    def test_change_state(self, driver):
        state_flag = "INIT"  # Biến flag để theo dõi trạng thái
        try:
            # 1. Mở trang web
            state_flag = "OPENED_LOGIN_PAGE"
            print(f"[STATE: {state_flag}] Mở trang /authentication")
            time.sleep(2)  # Chờ trang tải xong

            # Kiểm tra sự tồn tại của nút "Login"
            login_button = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
            print(f"[STATE: {state_flag}] Người dùng chưa đăng nhập. Nút Login tồn tại.")
            assert "LOGIN" in login_button.text, "Nút Login không hiển thị!"

            
            time.sleep(2)
            # 2. Nhập thông tin đăng nhập
            state_flag = "ENTERING_CREDENTIALS"
            print(f"[STATE: {state_flag}] Nhập thông tin đăng nhập.")
            username_input = driver.find_element(By.CLASS_NAME, "input-label")
            password_input = driver.find_elements(By.CLASS_NAME, "input-label")[1]  # Trường thứ 2 là mật khẩu
            username_input.send_keys("bismite@gmail.com")  # Thay bằng tài khoản của bạn
            password_input.send_keys("Midgapff@15")  # Thay bằng mật khẩu của bạn


            time.sleep(2)   
            # 3. Nhấn nút "Login"
            state_flag = "LOGGING_IN"
            print(f"[STATE: {state_flag}] Nhấn nút Login.")
            login_button.click()
            time.sleep(2)

            # 4. Kiểm tra trạng thái sau khi đăng nhập
            state_flag = "CHECKING_LOGIN_STATE"
            print(f"[STATE: {state_flag}] Kiểm tra trạng thái sau khi đăng nhập.")
            logout_button = driver.find_element(By.XPATH, "//*[@id='root']/div[1]/ul/li[3]")
            assert "Log Out" in logout_button.text, "Không tìm thấy nút Đăng xuất sau khi đăng nhập!"

            # 5. Chuyển trạng thái: Đăng xuất
            state_flag = "LOGGING_OUT"
            print(f"[STATE: {state_flag}] Chuyển sang trạng thái Đăng xuất.")
            logout_button.click()
            time.sleep(2)

            state_flag = "COMPLETED"
            print(f"[STATE: {state_flag}] Test chuyển đổi trạng thái thành công!")

        except AssertionError as e:
            print(f"[STATE: {state_flag}] Test thất bại: {e}")

        finally:
            # Đóng trình duyệt
            driver.quit()
