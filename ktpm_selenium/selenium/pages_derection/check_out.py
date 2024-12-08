import time

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.keys import Keys


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    # go to home page
    def go_to_check_out_when_logged_in(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[1]/a/button").click()
        time.sleep(3)
        # next on shipping
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/a[2]/button").click()
        time.sleep(3)
        # next on payment
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/a[2]/button").click()
        time.sleep(3)

    def search_and_add_to_basket(self):
        PRODUCTS = ["Adidas Ultra Boost", "Vans Old Skool", "Converse Chuck Taylor All Star", "Nike Air Max 270"]
        # Chọn sản phẩm ngẫu nhiên từ danh sách
        random_product = random.choice(PRODUCTS)
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/nav/div[2]/ul/li[1]/a").click()
        time.sleep(2)
        # Tìm kiếm thanh tìm kiếm
        search_box = self.driver.find_element(By.ID, "search")  # Thay "q" bằng name hoặc id của thanh tìm kiếm
        search_box.clear()
        search_box.send_keys(random_product)
        search_box.send_keys(Keys.RETURN)

        # Chờ kết quả hiển thị
        time.sleep(3)

        # Nhấn vào sản phẩm đầu tiên trong danh sách
        first_product = self.driver.find_element(By.CLASS_NAME,
                                                 "product-card")  # Chỉnh sửa selector cho đúng trang của bạn
        first_product.click()

        # Chờ để trang chi tiết sản phẩm tải
        time.sleep(3)

        # Tìm và nhấn nút "Add to Basket"
        add_to_basket_button = self.driver.find_element(By.XPATH,
                                                        "/html/body/div/div[1]/div[2]/div[2]/button[1]")  # Thay bằng ID hoặc selector của nút
        add_to_basket_button.click()

        # Xác nhận thêm sản phẩm vào giỏ thành công (tuỳ trang)
        time.sleep(2)

    def go_to_check_out_when_not_logged_in(self, email, password):
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[1]/a/button").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div/div/div[1]/div/div/div/form/label[1]/div/input").send_keys(
            email
        )
        self.driver.find_element(By.XPATH,
                                 "/html/body/div/div/div/div[1]/div/div/div/form/label[2]/div/input").send_keys(
            password
        )
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/form/button").click()
        time.sleep(5)

        self.driver.find_element(By.XPATH, "/html/body/div/nav/div[2]/div/a[3]/div").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[1]/a/button").click()
        time.sleep(2)
        # next on shipping
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/a[2]/button").click()
        time.sleep(3)
        # next on payment
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[2]/a[2]/button").click()
        time.sleep(3)

    def scroll_to_element(self, element):
        """Cuộn đến một phần tử cụ thể trên trang."""
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        time.sleep(1)

    #chose paypal in 3000/checkout
    def chose_paypal(self):
        time.sleep(10)
        iframe_elements = self.driver.find_elements(By.TAG_NAME, "iframe")

        # Chuyển sang iframe đầu tiên
        self.driver.switch_to.frame(iframe_elements[0])

        # Tìm phần tử bên trong iframe
        element = self.driver.find_element(By.XPATH,
                                           "//div[@class='paypal-button-row paypal-button-number-0 paypal-button-layout-vertical paypal-button-number-multiple paypal-button-env-sandbox paypal-button-color-blue paypal-button-text-color-white paypal-logo-color-white   paypal-button-shape-rect']")

        # Tương tác với phần tử (ví dụ: click)
        element.click()
        time.sleep(10)

    def pay_with_paypal(self, email_paypal, password_paypal):
        # Chuyển sang cửa sổ mới
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])
        print("Danh sách cửa sổ:", self.driver.window_handles)
        print("Tiêu đề cửa sổ hiện tại:", self.driver.title)

        try:
            # Chờ đến khi phần tử input email xuất hiện
            email_input = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, "//input[@id='email']"))
            )
            print("Phần tử email input đã sẵn sàng.")

            # Cuộn phần tử vào tầm nhìn nếu cần thiết
            self.driver.execute_script("arguments[0].scrollIntoView(true);", email_input)
            email_input.send_keys(email_paypal)

            # Nhấn nút tiếp tục
            continue_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@class='button actionContinue scTrack:unifiedlogin-login-click-next']"))
            )
            continue_button.click()
            print("Đã nhấn nút tiếp tục.")

            # Loại bỏ dấu nháy nếu có trong giá trị cần nhập
            password_paypal = password_paypal.replace('"', '').replace("'", "").strip()

            # Chờ đến khi phần tử input password có thể tương tác
            password_input = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))
            )
            print("Phần tử password input đã sẵn sàng.")

            # Xóa giá trị cũ (nếu có) trước khi nhập
            password_input.clear()

            # Nhập thông tin vào ô password
            password_input.send_keys(password_paypal)

            # Nhấn nút tiếp tục
            login_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(
                    (By.XPATH, "//button[@class='button actionContinue scTrack:unifiedlogin-login-submit']"))
            )
            login_button.click()
            print("Đã nhấn nút login.")

            # Chờ đến khi phần tử xuất hiện
            checkout_Button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH,
                     "//button[@class='Buttons_base_2xi07 CheckoutButton_noMargin_mv-3h xo-member-c72rwi-button_base-text_button_lg-btn_full_width']"))
            )
            print("checkout san sang ")
            checkout_Button.click()
            time.sleep(10)

        except TimeoutException:
            print("Không tìm thấy phần tử. Vui lòng kiểm tra lại locator hoặc tốc độ tải.")
        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}")

    def login_paypal_email(self, email_paypal):
        # Chuyển sang cửa sổ mới
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        # Chờ đến khi phần tử input email xuất hiện
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='email']"))
        )

        # Cuộn phần tử vào tầm nhìn nếu cần thiết
        self.driver.execute_script("arguments[0].scrollIntoView(true);", email_input)
        email_input.send_keys(email_paypal)

        # Nhấn nút tiếp tục
        continue_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@class='button actionContinue scTrack:unifiedlogin-login-click-next']"))
        )
        continue_button.click()

    def login_paypal(self, email_paypal, password_paypal):
        # Chuyển sang cửa sổ mới
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[-1])

        # Chờ đến khi phần tử input email xuất hiện
        email_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//input[@id='email']"))
        )

        # Cuộn phần tử vào tầm nhìn nếu cần thiết
        self.driver.execute_script("arguments[0].scrollIntoView(true);", email_input)
        email_input.send_keys(email_paypal)

        # Nhấn nút tiếp tục
        continue_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@class='button actionContinue scTrack:unifiedlogin-login-click-next']"))
        )
        continue_button.click()
        # Loại bỏ dấu nháy nếu có trong giá trị cần nhập
        password_paypal = password_paypal.replace('"', '').replace("'", "").strip()

        # Chờ đến khi phần tử input password có thể tương tác
        password_input = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@id='password']"))
        )

        # Xóa giá trị cũ (nếu có) trước khi nhập
        password_input.clear()

        # Nhập thông tin vào ô password
        password_input.send_keys(password_paypal)

        # Nhấn nút tiếp tục
        login_button = WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@class='button actionContinue scTrack:unifiedlogin-login-submit']"))
        )
        login_button.click()

    def get_totals_paypal(self):
        totals_paypal_text = self.driver.find_element(By.XPATH,
                                                      "/html/body/div[2]/div/div/div/header/div[2]/div[3]/div/div/button/span").text

        # Xử lý chuỗi và chuyển đổi thành số thực
        totals_paypal = float(totals_paypal_text.replace("kr", "")  # Loại bỏ "kr"
                              .replace(",", "")  # Loại bỏ dấu phẩy
                              .replace("DKK", "")  # Loại bỏ "DKK"
                              .replace("&nbsp;", "")  # Loại bỏ các khoảng trắng không thể nhìn thấy
                              .strip())  # Loại bỏ khoảng trắng thừa

        return totals_paypal

    def chose_debit_credit_card(self):
        time.sleep(10)
        iframe_elements = self.driver.find_elements(By.TAG_NAME, "iframe")

        # Chuyển sang iframe đầu tiên
        self.driver.switch_to.frame(iframe_elements[0])

        # Tìm phần tử bên trong iframe
        element = self.driver.find_element(By.XPATH, "/html/body/div/div/div[2]/div")

        # Tương tác với phần tử (ví dụ: click)
        element.click()
        time.sleep(10)

    def chose_visa(self):
        time.sleep(2)
        self.scroll_to_element(self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/main/div[2]/section[1]/div[4]/div[3]/div/div[1]/div[1]/div/label/span"))
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[2]/div/div/div[1]/main/div[2]/section[1]/div[4]/div[3]/div/div[1]/div[1]/div/label/span").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/main/div[3]/div[2]/button").click()
        time.sleep(2)

    def chose_paypal_credit(self):
        time.sleep(2)
        self.scroll_to_element(self.driver.find_element(By.XPATH, "//main/div[2]/section[1]/div[4]/div[4]/div[1]/div/label/span/span"))
        self.driver.find_element(By.XPATH, "//main/div[2]/section[1]/div[4]/div[4]/div[1]/div/label/span/span").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/main/div[3]/div[2]/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/article/section/div/div/main/div/div/form/div[2]/div/div/div/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[3]/div/div[2]/article/section/div/div/div[2]/div[2]/div/button[1]").click()
        time.sleep(2)
        #number
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/article/section/div/div/main/div/div/form/div[1]/div[2]/div[2]/div[2]/div/div/input").send_keys("(914) 465-0305")
        time.sleep(2)
        #date of birth
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[2]/div/div[2]/article/section/div/div/main/div/div/form/div[1]/div[2]/div[4]/div/div/input").send_keys("11 11 1999")
        time.sleep(2)
        # SSN last 4
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[2]/div/div[2]/article/section/div/div/main/div/div/form/div[1]/div[2]/div[5]/div/div/input").send_keys("1111")
        time.sleep(2)
        #annual income after taxes
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[2]/div/div[2]/article/section/div/div/main/div/div/form/div[1]/div[2]/div[6]/div/div/div[1]/input").send_keys("100000")
        time.sleep(2)
        #confirm
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div[2]/article/section/div/div/main/div/div/form/div[2]/div/div/div/button").click()

        #accept terms and conditions
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[2]/div/div[2]/article/section/div/div/main/div/div/div[2]/div/div/div[2]/button").click()
        time.sleep(2)

        #Agree
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[3]/div/div[2]/article/footer/div/div/button").click()
        time.sleep(2)
        #return to check out
        self.driver.find_element(By.XPATH,
                                 "/html/body/div[2]/div/div[2]/article/section/div/div/main/div/div[2]/div/div/div/button").click()
        time.sleep(2)

        #complete payment
        self.driver.find_element(By.XPATH,"/html/body/div[2]/div/div/div/main/div[4]/div[2]/button").click()
        time.sleep(2)
    def pay_with_debit_credit_card(self, card_number, expiry_date, cvv, first_name, last_name, address, apt, city,
                                   zip_code, phone, email):
        # Tìm và chuyển vào iframe nếu cần
        iframe = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.TAG_NAME, "iframe"))
        )
        self.driver.switch_to.frame(iframe)

        # Card number
        card_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/form/div/div[2]/div/div[1]/div/div/div/input"))
        )
        self.scroll_to_element(card_input)
        card_input.send_keys(card_number)
        time.sleep(1)
        # Expiry date
        expiry_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/form/div/div[3]/div[1]/div[1]/input"))
        )
        self.scroll_to_element(expiry_input)
        expiry_input.send_keys(expiry_date)
        time.sleep(1)
        # CVV
        cvv_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div/form/div/div[3]/div[3]/div/input"))
        )
        self.scroll_to_element(cvv_input)
        cvv_input.send_keys(cvv)
        time.sleep(1)

        # Chọn thẳng tới quốc gia Vietnam từ XPATH của option[199]
        # country_option = WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, "/html/body/div[1]/div/div/form/div/div[4]/div[1]/div/div/div/select/option[199]")
        #     )
        # )
        # self.scroll_to_element(country_option)  # Cuộn tới phần tử nếu cần
        # country_option.click()  # Chọn option
        # time.sleep(1)

        # First name
        first_name_input = self.driver.find_element(By.ID, "billingAddress.givenName")
        self.scroll_to_element(first_name_input)
        first_name_input.send_keys(first_name)
        time.sleep(1)

        # Last name
        last_name_input = self.driver.find_element(By.ID, "billingAddress.familyName")
        self.scroll_to_element(last_name_input)
        last_name_input.send_keys(last_name)
        time.sleep(1)

        # Address
        address_input = self.driver.find_element(By.ID, "billingAddress.line1")
        self.scroll_to_element(address_input)
        address_input.send_keys(address)
        time.sleep(1)

        # Apt
        apt_input = self.driver.find_element(By.ID, "billingAddress.line2")
        self.scroll_to_element(apt_input)
        apt_input.send_keys(apt)
        time.sleep(1)

        # City
        city_input = self.driver.find_element(By.ID, "billingAddress.city")
        self.scroll_to_element(city_input)
        city_input.send_keys(city)
        time.sleep(1)

        # Chọn thành phố từ option[9]
        city_option = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/form/div/div[4]/div[3]/div[4]/div/div/div/select/option[9]")
            )
        )
        self.scroll_to_element(city_option)  # Cuộn tới phần tử nếu cần
        city_option.click()  # Chọn thành phố từ option[30]
        time.sleep(1)

        # ZIP code
        postcode_input = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[1]/div/div/form/div/div[4]/div[3]/div[5]/div/div/input"))
        )
        postcode_input.send_keys(zip_code)

        # Phone
        phone_input = self.driver.find_element(By.ID, "phone")
        self.scroll_to_element(phone_input)
        phone_input.send_keys(phone)
        time.sleep(1)

        # Email
        email_input = self.driver.find_element(By.ID, "email")
        self.scroll_to_element(email_input)
        email_input.send_keys(email)
        time.sleep(1)

        # radio_button = WebDriverWait(self.driver, 10).until(
        #     EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div/div/form/div/div[8]/div/div/label"))
        # )

        # Click vào phần tử radio button
        # radio_button.click()
        # time.sleep(1)

        # Click vào payment
        self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/form/div/div[9]/button").click()
        time.sleep(1)

        # Quay lại ngữ cảnh chính
        self.driver.switch_to.default_content()

    # def error_label(self):
    #     self.driver.find_element(By.CLASS_NAME, "css-wjdwzz").text()
    #     time.sleep(1)

    # def message(self):
    #     time.sleep(10)
    #     iframe_elements = self.driver.find_elements(By.TAG_NAME, "iframe")
    #
    #     # Chuyển sang iframe đầu tiên
    #     self.driver.switch_to.frame(iframe_elements[0])
    #
    #     # Tìm phần tử bên trong iframe
    #     element = self.driver.find_element(By.XPATH, "(/html/body/div[1]/div/div/div)[1]")
    #
    #     # Tương tác với phần tử (ví dụ: click)
    #     element_text = element.text
    #     return element_text

    def message_success(self):
        time.sleep(5)
        element = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/h1")
        # Tương tác với phần tử (ví dụ: click)
        element_text = element.text
        return element_text

    def extract_and_calculate_totals(self, driver):
        """
            Hàm để trích xuất giá trị từ trang web và thực hiện tính toán tổng.
            """
        # Tìm và lấy dữ liệu từ các phần tử trên trang
        sub_totals_text = self.driver.find_element(By.XPATH,
                                                   "/html/body/div/div/div/div[1]/div/div[2]/div[3]/div[1]/p[2]").text
        shipping_text = self.driver.find_element(By.XPATH,
                                                 "/html/body/div/div/div/div[1]/div/div[2]/div[3]/div[2]/p[2]").text
        totals_text = self.driver.find_element(By.XPATH,
                                               "/html/body/div/div/div/div[1]/div/div[2]/div[3]/div[4]/p[2]").text

        # Xử lý chuỗi để chuyển đổi thành số thực
        subtotals = float(sub_totals_text.replace("kr.", "").replace(".", "").replace(",", ".").strip())
        shipping = float(shipping_text.replace("kr.", "").replace(".", "").replace(",", ".").strip())
        totals = float(totals_text.replace("kr.", "").replace(".", "").replace(",", ".").strip())

        # Tính tổng
        totals_calculated = subtotals + shipping

        # Trả về các giá trị cần thiết
        return subtotals, shipping, totals, totals_calculated

    def handle_alert(self):
        WebDriverWait(self.driver, 20).until(EC.alert_is_present())
        alert = self.driver.switch_to.alert
        alert.accept()

        print("Alert accepted successfully!")

    def error_label(self):
        self.scroll_to_element(self.driver.find_element(By.TAG_NAME, "iframe"))
        iframe = self.driver.find_element(By.TAG_NAME, "iframe")  # Thay đổi selector nếu cần
        self.driver.switch_to.frame(iframe)
        self.scroll_to_element(self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/form/div/div[2]/div/div[1]/div/div/div/input"))
        input_element = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/form/div/div[2]/div/div[1]/div/div/div/input").click

        # Lấy giá trị của thuộc tính aria-describedby (đây là ID của phần tử lỗi)
        error_message_id = input_element.get_attribute("aria-describedby")

        # Tìm phần tử lỗi sử dụng ID từ aria-describedby
        icon = self.driver.find_element(By.ID, error_message_id)

        return icon

    def get_error_message_login_paypal_email(self):
        error_message_login_paypal = self.driver.find_element(By.XPATH, "//p[@class='invalidError']")
        return error_message_login_paypal.text

    def get_error_message_login_paypal_password(self):
        error_message_login_paypal = self.driver.find_element(By.XPATH,
                                                              "/html/body/div[1]/section[1]/div[1]/div[2]/div[1]/p")
        return error_message_login_paypal.text

    def get_empty_error(self):
        error_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//div[contains(@class, 'errorMessage') and contains(@class, 'show')]"))
        )
        return error_element

    def cancel_checkout(self):
        self.scroll_to_element(self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/main/div[6]/a"))
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/main/div[6]/a").click()
        time.sleep(2)

    def add_debit_credit_card_paypal(self):
        self.scroll_to_element(self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/main/div[2]/div/div/button"))
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/main/div[2]/div/div/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/section/div/div[2]/form/div/div[2]/div[3]/div/div[1]/input").send_keys("4111 1111 1111 1111")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/section/div/div[2]/form/div/div[2]/div[3]/div/div[2]/div[1]/input").send_keys("01 25")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/section/div/div[2]/form/div/div[2]/div[3]/div/div[2]/div[2]/input").send_keys("123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div[1]/section/div/div[2]/form/div/button").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/main/div[4]/div[2]/button").click()