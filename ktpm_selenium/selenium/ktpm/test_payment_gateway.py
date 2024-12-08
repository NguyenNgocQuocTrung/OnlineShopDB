import time
from ktpm_selenium.selenium.utils.webdriver_setup import Driver
from ktpm_selenium.selenium.pages_derection.shopping_cart_page import ShoppingCartPage
from ktpm_selenium.selenium.pages_derection.check_out import CheckOutPage
from ktpm_selenium.selenium.ktpm.test_login import TestLogin
from ktpm_selenium.selenium.pages_derection.home_page import HomePage


class TestPaymentGateway_Credit_or_Debit(Driver):

    def login_and_add_product_to_basket(self, driver):
        # ktpm_selenium/selenium/ktpm/test_login
        test_login = TestLogin()

        # call back from pages_derection
        shopping_cart_page = ShoppingCartPage(driver)
        check_out_page = CheckOutPage(driver)

        # login
        test_login.test_login_valid_info(driver)
        check_out_page.search_and_add_to_basket()
        shopping_cart_page.go_to_shopping_cart()

        # skip step loggin in check out for logged in with valid info
        check_out_page.go_to_check_out_when_logged_in()

    def login_and_add_product_to_basket_without_login(self, driver):
        # call back from pages_derection
        home_page = HomePage(driver)
        shopping_cart_page = ShoppingCartPage(driver)
        check_out_page = CheckOutPage(driver)

        home_page.go_to_home_page()
        check_out_page.search_and_add_to_basket()
        shopping_cart_page.go_to_shopping_cart()
        # skip step loggin in check out for logged in with valid info
        email = "elroydevops@gmail.com"
        password = "0900000009"
        check_out_page.go_to_check_out_when_not_logged_in(email, password)

    def test_payment_gateway_not_logged_in(self, driver):
        self.login_and_add_product_to_basket_without_login(driver)
        check_out_page = CheckOutPage(driver)
        time.sleep(2)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"
        time.sleep(2)
        # chose kind of payment
        check_out_page.chose_debit_credit_card()

        # enter fields "valid info"
        card_number = "4111 1111 1111 1111"
        expiry_date = "01/25"
        cvv = "123"
        first_name = "elroy"
        last_name = "devops"
        address = "2 New York Street"
        apt = "123 Phan"
        city = "New York"
        zip_code = "90001"
        phone = "(914) 465-0305"
        email = "elroydevops@gmail.com"
        check_out_page.pay_with_debit_credit_card(card_number, expiry_date, cvv,
                                                  first_name, last_name, address, apt,
                                                  city,
                                                  zip_code, phone, email)

        time.sleep(5)

        check_out_page.handle_alert()

        time.sleep(2)

        message_error = check_out_page.message_success()  # Lấy thông báo lỗi từ iframe
        print(message_error)
        assert "confirmed" in message_error
        # Kiểm tra xem thông báo lỗi có chứa thông điệp mong đợi không

        driver.quit()
        time.sleep(5)

    def test_payment_gateway(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        # chose kind of payment
        check_out_page.chose_debit_credit_card()

        # enter fields "valid info"
        card_number = "4111 1111 1111 1111"
        expiry_date = "01/25"
        cvv = "123"
        first_name = "elroy"
        last_name = "devops"
        address = "2 New York Street"
        apt = "123 Phan"
        city = "New York"
        zip_code = "90001"
        phone = "(914) 465-0305"
        email = "elroydevops@gmail.com"
        check_out_page.pay_with_debit_credit_card(card_number, expiry_date, cvv,
                                                  first_name, last_name, address, apt,
                                                  city,
                                                  zip_code, phone, email)

        time.sleep(5)

        check_out_page.handle_alert()

        time.sleep(2)

        message_error = check_out_page.message_success()  # Lấy thông báo lỗi từ iframe
        print(message_error)
        assert "confirmed" in message_error
        # Kiểm tra xem thông báo lỗi có chứa thông điệp mong đợi không

        driver.quit()
        time.sleep(5)

    def test_payment_paypal(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        check_out_page.chose_paypal()
        time.sleep(1)

        email_paypal = "sb-wwcid34547417@personal.example.com"
        password_paypal = "KW.G0FQl"
        check_out_page.pay_with_paypal(email_paypal, password_paypal)
        time.sleep(5)

        totals_paypal = check_out_page.get_totals_paypal()
        assert totals_calculated == totals_paypal, "ok"

        time.sleep(5)
        original_window = driver.window_handles
        driver.switch_to.window(original_window[0])
        print("Đã chuyển lại về cửa sổ gốc")

        check_out_page.handle_alert()

        time.sleep(10)
        message_error = check_out_page.message_success()  # Lấy thông báo lỗi từ iframe
        print(message_error)
        assert "confirmed" in message_error

        driver.quit()
        time.sleep(5)

    def test_paypal_cancel_and_return_checkout(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        # Chọn thanh toán bằng PayPal
        check_out_page.chose_paypal()
        time.sleep(1)

        email_paypal = "sb-wwcid34547417@personal.example.com"
        password_paypal = "KW.G0FQl"
        check_out_page.login_paypal(email_paypal, password_paypal)
        time.sleep(5)

        totals_paypal = check_out_page.get_totals_paypal()
        assert totals_calculated == totals_paypal, "ok"

        # Mô phỏng tình huống tắt cửa sổ thanh toán
        time.sleep(5)
        original_window = driver.window_handles[0]  # Cửa sổ gốc
        payment_window = driver.window_handles[1]  # Cửa sổ thanh toán (PayPal)

        # Chuyển sang cửa sổ thanh toán
        driver.switch_to.window(payment_window)

        check_out_page.cancel_checkout()

        # Chuyển lại về cửa sổ gốc
        driver.switch_to.window(original_window)

        # Kiểm tra trạng thái của cửa sổ gốc
        assert "checkout" in driver.current_url

        driver.quit()
        time.sleep(5)

    def test_paypal_visa_card(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        check_out_page.chose_paypal()
        time.sleep(1)

        email_paypal = "sb-wwcid34547417@personal.example.com"
        password_paypal = "KW.G0FQl"
        check_out_page.login_paypal(email_paypal, password_paypal)
        time.sleep(5)

        totals_paypal = check_out_page.get_totals_paypal()
        assert totals_calculated == totals_paypal, "ok"

        check_out_page.chose_visa()

        time.sleep(5)
        original_window = driver.window_handles
        driver.switch_to.window(original_window[0])
        print("Đã chuyển lại về cửa sổ gốc")

        check_out_page.handle_alert()

        time.sleep(10)
        message_error = check_out_page.message_success()  # Lấy thông báo lỗi từ iframe
        print(message_error)
        assert "confirmed" in message_error

        driver.quit()
        time.sleep(5)

    def test_paypal_credit_card(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        check_out_page.chose_paypal()
        time.sleep(1)

        email_paypal = "sb-wwcid34547417@personal.example.com"
        password_paypal = "KW.G0FQl"
        check_out_page.login_paypal(email_paypal, password_paypal)
        time.sleep(5)

        totals_paypal = check_out_page.get_totals_paypal()
        assert totals_calculated == totals_paypal, "ok"

        check_out_page.chose_paypal_credit()

        time.sleep(5)
        original_window = driver.window_handles
        driver.switch_to.window(original_window[0])
        print("Đã chuyển lại về cửa sổ gốc")

        check_out_page.handle_alert()

        time.sleep(10)
        message_error = check_out_page.message_success()  # Lấy thông báo lỗi từ iframe
        print(message_error)
        assert "confirmed" in message_error

        driver.quit()
        time.sleep(5)

    def test_paypay_add_debit_credit_card(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        check_out_page.chose_paypal()
        time.sleep(10)

        email_paypal = "sb-wwcid34547417@personal.example.com"
        password_paypal = "KW.G0FQl"
        check_out_page.login_paypal(email_paypal, password_paypal)
        time.sleep(5)

        totals_paypal = check_out_page.get_totals_paypal()
        assert totals_calculated == totals_paypal, "ok"

        check_out_page.add_debit_credit_card_paypal()

        time.sleep(5)
        original_window = driver.window_handles
        driver.switch_to.window(original_window[0])
        print("Đã chuyển lại về cửa sổ gốc")

        check_out_page.handle_alert()

        time.sleep(5)
        message_error = check_out_page.message_success()  # Lấy thông báo lỗi từ iframe
        print(message_error)
        assert "confirmed" in message_error

        driver.quit()
        time.sleep(5)

    def test_payment_gateway_wrongemail(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        # chose kind of payment
        check_out_page.chose_debit_credit_card()

        # enter fields "valid info"
        card_number = "4111 1111 1111 1111"
        expiry_date = "01/25"
        cvv = "123"
        first_name = "elroy"
        last_name = "devops"
        address = "2 New York Street"
        apt = "123 Phan"
        city = "New York"
        zip_code = "90001"
        phone = "(914) 465-0305"
        email = "elroydevopsgmail.com"
        check_out_page.pay_with_debit_credit_card(card_number, expiry_date, cvv,
                                                  first_name, last_name, address, apt,
                                                  city,
                                                  zip_code, phone, email)
        time.sleep(2)

        assert "checkout" in driver.current_url
        time.sleep(2)
        driver.quit()
        time.sleep(5)

    def test_payment_gateway_wrongnumber(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        # chose kind of payment
        check_out_page.chose_debit_credit_card()

        # enter fields "valid info"
        card_number = "4111 1111 1111 1111"
        expiry_date = "01/25"
        cvv = "123"
        first_name = "elroy"
        last_name = "devops"
        address = "2 New York Street"
        apt = "123 Phan"
        city = "New York"
        zip_code = "90001"
        phone = "666666666666"
        email = "elroydevops@gmail.com"
        check_out_page.pay_with_debit_credit_card(card_number, expiry_date, cvv,
                                                  first_name, last_name, address, apt,
                                                  city,
                                                  zip_code, phone, email)
        time.sleep(2)

        assert "checkout" in driver.current_url
        time.sleep(2)
        driver.quit()
        time.sleep(5)

    def test_payment_gateway_wrongzipcode(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        # chose kind of payment
        check_out_page.chose_debit_credit_card()

        # enter fields "valid info"
        card_number = "4111 1111 1111 1111"
        expiry_date = "01/25"
        cvv = "123"
        first_name = "elroy"
        last_name = "devops"
        address = "2 New York Street"
        apt = "123 Phan"
        city = "New York"
        zip_code = "2222222"
        phone = "(914) 465-0305"
        email = "elroydevops@gmail.com"
        check_out_page.pay_with_debit_credit_card(card_number, expiry_date, cvv,
                                                  first_name, last_name, address, apt,
                                                  city,
                                                  zip_code, phone, email)
        time.sleep(2)

        assert "checkout" in driver.current_url
        time.sleep(2)
        driver.quit()
        time.sleep(5)

    def test_payment_gateway_blankcity(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        # chose kind of payment
        check_out_page.chose_debit_credit_card()

        # enter fields "valid info"
        card_number = "4111 1111 1111 1111"
        expiry_date = "01/25"
        cvv = "123"
        first_name = "elroy"
        last_name = "devops"
        address = "2 New York Street"
        apt = "123 Phan"
        city = ""
        zip_code = "90001"
        phone = "(914) 465-0305"
        email = "elroydevops@gmail.com"
        check_out_page.pay_with_debit_credit_card(card_number, expiry_date, cvv,
                                                  first_name, last_name, address, apt,
                                                  city,
                                                  zip_code, phone, email)
        time.sleep(2)

        assert "checkout" in driver.current_url
        time.sleep(2)
        driver.quit()
        time.sleep(5)

    def test_payment_gateway_blankaddress(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        # chose kind of payment
        check_out_page.chose_debit_credit_card()

        # enter fields "valid info"
        card_number = "4111 1111 1111 1111"
        expiry_date = "01/25"
        cvv = "123"
        first_name = "elroy"
        last_name = "devops"
        address = ""
        apt = "123 Phan"
        city = "New York"
        zip_code = "90001"
        phone = "(914) 465-0305"
        email = "elroydevops@gmail.com"
        check_out_page.pay_with_debit_credit_card(card_number, expiry_date, cvv,
                                                  first_name, last_name, address, apt,
                                                  city,
                                                  zip_code, phone, email)
        time.sleep(2)

        assert "checkout" in driver.current_url
        time.sleep(2)
        driver.quit()
        time.sleep(5)

    def test_payment_gateway_blanklastname(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        # chose kind of payment
        check_out_page.chose_debit_credit_card()

        # enter fields "valid info"
        card_number = "4111 1111 1111 1111"
        expiry_date = "01/25"
        cvv = "123"
        first_name = "elroy"
        last_name = ""
        address = "2 New York Street"
        apt = "123 Phan"
        city = "New York"
        zip_code = "90001"
        phone = "(914) 465-0305"
        email = "elroydevops@gmail.com"
        check_out_page.pay_with_debit_credit_card(card_number, expiry_date, cvv,
                                                  first_name, last_name, address, apt,
                                                  city,
                                                  zip_code, phone, email)
        time.sleep(2)

        assert "checkout" in driver.current_url
        time.sleep(2)
        driver.quit()
        time.sleep(5)

    def test_payment_gateway_blankfirstname(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        # chose kind of payment
        check_out_page.chose_debit_credit_card()

        # enter fields "valid info"
        card_number = "4111 1111 1111 1111"
        expiry_date = "01/25"
        cvv = "123"
        first_name = ""
        last_name = "devops"
        address = "2 New York Street"
        apt = "123 Phan"
        city = "New York"
        zip_code = "90001"
        phone = "(914) 465-0305"
        email = "elroydevops@gmail.com"
        check_out_page.pay_with_debit_credit_card(card_number, expiry_date, cvv,
                                                  first_name, last_name, address, apt,
                                                  city,
                                                  zip_code, phone, email)
        time.sleep(2)

        assert "checkout" in driver.current_url
        time.sleep(2)
        driver.quit()
        time.sleep(5)

    def test_payment_gateway_blankcvv(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        # chose kind of payment
        check_out_page.chose_debit_credit_card()

        # enter fields "valid info"
        card_number = "4111 1111 1111 1111"
        expiry_date = "01/25"
        cvv = ""
        first_name = "elroy"
        last_name = "devops"
        address = "2 New York Street"
        apt = "123 Phan"
        city = "New York"
        zip_code = "90001"
        phone = "(914) 465-0305"
        email = "elroydevops@gmail.com"
        check_out_page.pay_with_debit_credit_card(card_number, expiry_date, cvv,
                                                  first_name, last_name, address, apt,
                                                  city,
                                                  zip_code, phone, email)
        time.sleep(2)

        assert "checkout" in driver.current_url
        driver.quit()
        time.sleep(5)

    def test_payment_gateway_wrongexpirydate(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        # chose kind of payment
        check_out_page.chose_debit_credit_card()

        # enter fields "valid info"
        card_number = "4111 1111 1111 1111"
        expiry_date = "01/22"
        cvv = "123"
        first_name = "elroy"
        last_name = "devops"
        address = "2 New York Street"
        apt = "123 Phan"
        city = "New York"
        zip_code = "90001"
        phone = "(914) 465-0305"
        email = "elroydevops@gmail.com"
        check_out_page.pay_with_debit_credit_card(card_number, expiry_date, cvv,
                                                  first_name, last_name, address, apt,
                                                  city,
                                                  zip_code, phone, email)
        time.sleep(2)

        assert "checkout" in driver.current_url
        time.sleep(2)
        driver.quit()
        time.sleep(5)

    def test_payment_gateway_wrongcardnumber(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        # chose kind of payment
        check_out_page.chose_debit_credit_card()

        # enter fields "valid info"
        card_number = "4111 1111 6666 3333"
        expiry_date = "01/25"
        cvv = "123"
        first_name = "elroy"
        last_name = "devops"
        address = "2 New York Street"
        apt = "123 Phan"
        city = "New York"
        zip_code = "90001"
        phone = "(914) 465-0305"
        email = "elroydevops@gmail.com"
        check_out_page.pay_with_debit_credit_card(card_number, expiry_date, cvv,
                                                  first_name, last_name, address, apt,
                                                  city,
                                                  zip_code, phone, email)
        time.sleep(2)

        assert "checkout" in driver.current_url
        time.sleep(2)
        driver.quit()
        time.sleep(5)

    def test_payment_gateway_blankallfields(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        # chose kind of payment
        check_out_page.chose_debit_credit_card()

        # enter fields "valid info"
        card_number = ""
        expiry_date = ""
        cvv = ""
        first_name = ""
        last_name = ""
        address = ""
        apt = ""
        city = ""
        zip_code = ""
        phone = ""
        email = ""
        check_out_page.pay_with_debit_credit_card(card_number, expiry_date, cvv,
                                                  first_name, last_name, address, apt,
                                                  city,
                                                  zip_code, phone, email)
        time.sleep(2)

        assert "checkout" in driver.current_url

        time.sleep(5)


    def test_payment_paypal_error_email(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        check_out_page.chose_paypal()
        time.sleep(10)

        email_paypal = "sb-wwcid34547417personal.example.com"
        check_out_page.login_paypal_email(email_paypal)
        time.sleep(5)

        error = check_out_page.get_error_message_login_paypal_email()
        assert "isn’t right" in error
        driver.quit()
        time.sleep(5)

    def test_payment_paypal_empty_email(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        check_out_page.chose_paypal()
        time.sleep(1)

        email_paypal = ""
        check_out_page.login_paypal_email(email_paypal)
        time.sleep(5)

        error = check_out_page.get_empty_error()
        assert error

        time.sleep(5)
        driver.quit()
        time.sleep(5)

    def test_payment_paypal_error_password(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        check_out_page.chose_paypal()
        time.sleep(1)

        email_paypal = "sb-wwcid34547417@personal.example.com"
        password_paypal = "123445"
        check_out_page.login_paypal(email_paypal, password_paypal)
        time.sleep(5)

        error = check_out_page.get_error_message_login_paypal_password()
        assert "Try again" in error
        driver.quit()
        time.sleep(5)

    def test_payment_paypal_empty_password(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        check_out_page.chose_paypal()
        time.sleep(11)

        email_paypal = "sb-wwcid34547417@personal.example.com"
        password_paypal = ""
        check_out_page.login_paypal(email_paypal, password_paypal)
        time.sleep(5)

        error = check_out_page.get_empty_error()
        assert error
        time.sleep(5)
        driver.quit()
        time.sleep(5)

    def test_paypal_wrong_when_checkout(self, driver):
        self.login_and_add_product_to_basket(driver)
        check_out_page = CheckOutPage(driver)

        # calculate totals for assert
        extract_and_calculate_totals = check_out_page.extract_and_calculate_totals(driver)
        subtotals, shipping, totals, totals_calculated = extract_and_calculate_totals

        assert totals_calculated == totals, f"Total mismatch: Expected {totals_calculated}, but got {totals}"

        # Chọn thanh toán bằng PayPal
        check_out_page.chose_paypal()
        time.sleep(1)

        email_paypal = "sb-wwcid34547417@personal.example.com"
        password_paypal = "KW.G0FQl"
        check_out_page.pay_with_paypal(email_paypal, password_paypal)
        time.sleep(5)

        totals_paypal = check_out_page.get_totals_paypal()
        assert totals_calculated == totals_paypal, "ok"

        # Mô phỏng tình huống tắt cửa sổ thanh toán
        time.sleep(5)
        original_window = driver.window_handles[0]  # Cửa sổ gốc
        payment_window = driver.window_handles[1]  # Cửa sổ thanh toán (PayPal)

        # Chuyển sang cửa sổ thanh toán
        driver.switch_to.window(payment_window)
        print("Đã chuyển sang cửa sổ thanh toán.")

        # Đóng cửa sổ thanh toán
        driver.close()
        print("Cửa sổ thanh toán đã bị tắt.")

        # Chuyển lại về cửa sổ gốc
        driver.switch_to.window(original_window)
        print("Đã chuyển lại về cửa sổ gốc.")

        # Kiểm tra trạng thái của cửa sổ gốc
        assert "checkout" in driver.current_url
        print("Đang ở đúng trang checkout.")

        driver.quit()
        time.sleep(5)

