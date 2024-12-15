import pytest
from selenium.webdriver.common.by import By
from pages.authentication_page import LoginPage
from pages.shop import Shop
from pages.cart import Cart
from constants.elements_path import ElementsPath
from utilities import helper as hp
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestLogin:
    @pytest.fixture
    def setup(self,driver):
        login_page = LoginPage(driver)
        login_page.redirect_self()
        return login_page

#email=valid. password=valid, registered
    def test_login_with_valid_email_and_password_registered(self,setup):
        setup.enter_email("elroydevops@gmail.com")
        setup.enter_password("0900000009")
        setup.click_login()
        hp.assert_current_url_equals_account_url(setup.driver)

#================================================================================

class TestAdding:
    
    @pytest.fixture
    def setup(self,driver):
        self.driver = driver
        login_page = LoginPage(driver)
        login_page.redirect_self()
        login_page.enter_email("elroydevops@gmail.com")
        login_page.enter_password("0900000009")
        login_page.click_login()
        shop = Shop(driver)
        shop.sleep(0.8)
        shop.redirect_self()
        return shop

    @pytest.fixture
    def setup_cart(self, driver):
        self.driver = driver
        login_page = LoginPage(driver)
        login_page.redirect_self()
        login_page.enter_email("elroydevops@gmail.com")
        login_page.enter_password("0900000009")
        login_page.click_login()
        shop = Shop(driver)
        shop.sleep(0.8) 
        shop.redirect_self()
        self.test_add_multi_random_item(shop)
        cart = Cart(driver)
        cart.redirect_self()
        return cart
    
    def get_clickable_element(self, driver, by: By, arg, timeout = 10):
        element = WebDriverWait(driver, timeout).until(
            EC.element_to_be_clickable((by, arg))
        )
        return element
    
    def key_press(self, key: Keys):
        self.driver.find_element(By.XPATH, "//body").send_keys(key)
    
    def get_cart(self, driver):
        cart = Cart(driver)
        return cart
    
    #Test lấy item đầu tiên
    def test_click_item(self, setup):
        item_no = 1
        setup.click_item(item_no)
    
    #Test click random item
    def test_random_click_item(self, setup):
        item_no = hp.random_number_in_range(1, 8)
        setup.click_item(item_no)

    def test_random_choose_item_size(self, setup):
        self.test_random_click_item(setup)
        no_available_sizes = setup.get_no_available_sizes()
        random_size = hp.random_number_in_range(1, no_available_sizes)
        setup.get_size_by_option_index(random_size)

    #Test add random + size giày
    def test_add_random_item(self, setup):
        #Chọn random item từ shop
        rd_item_index = hp.random_number_in_range(1, 8)
        setup.click_item(rd_item_index)

        setup.sleep(0.8)
        #random size giày
        no_available_sizes = setup.get_no_available_sizes()
        random_size = hp.random_number_in_range(0, no_available_sizes-1)
        setup.sleep(0.8)
        setup.get_size_by_option_index(random_size)
        setup.add_item()

        #Kiểm tra nếu minicart hoạt động
        hp.assert_text_in_message(setup, ElementsPath.MINI_CART.NO_ITEM, "1")

    def test_add_multi_random_item(self, setup):
        no_items = hp.random_number_in_range(2, 4)

        for i in range(0, no_items):
            setup.redirect_self()                                           #Quay về shop
            setup.sleep(0.2)
            rd_item_index = hp.random_number_in_range(1, 8)                 #Lấy só random
            setup.click_item(rd_item_index)
            no_available_sizes = setup.get_no_available_sizes()
            random_size = hp.random_number_in_range(0, no_available_sizes-1)
            setup.sleep(0.2)
            setup.get_size_by_option_index(random_size)                     #Lấy randomsize theo thứ tự trong lựa chọn size
            setup.add_item()
        
        hp.assert_text_in_message(setup, ElementsPath.MINI_CART.NO_ITEM, f"{no_items}") #Kiểm tra nếu số lượng thêm = số lượng hiển thị trên minicart


    def test_check_item_in_cart(self, setup):
        #Chọn random item từ shop
        item_no = hp.random_number_in_range(1, 8)
        setup.click_item(item_no)

        setup.sleep(0.5)
        #random size giày
        no_available_sizes = setup.get_no_available_sizes()
        random_size = hp.random_number_in_range(1, no_available_sizes)
        current_shoe_name = setup.get_item_name()
        setup.get_size_by_option_index(random_size)
        setup.add_item()
        
        cart = self.get_cart(self.driver)
        cart.redirect_self()
        name = cart.get_item_name_by_index(1)
        assert current_shoe_name == name

    #Thêm vào giỏ hàng nhưng nếu cùng size giày thì dù có khác giày vẫn không thêm mới vào được, 
    # chỉ tăng số lượng cái giày đầu tiên của size đó
    def test_check_cart_after_add_multi_items_with_random_size(self, setup):
        item_list = {}
        no_items = hp.random_number_in_range(2, 5)

        for i in range(0, no_items):
            setup.redirect_self()                                           #Quay về shop
            rd_item_index = hp.random_number_in_range(1, 8)                 #Lấy số random
            while item_list.get(rd_item_index):
                rd_item_index = hp.random_number_in_range(2, 8)
            
            setup.click_item(rd_item_index)
            current_shoe_name = setup.get_item_name()
            item_list[rd_item_index] = current_shoe_name
            
            no_available_sizes = setup.get_no_available_sizes()
            random_size = hp.random_number_in_range(1, no_available_sizes-1)
            setup.sleep(0.2)
            setup.get_size_by_option_index(random_size)                     #Lấy randomsize theo thứ tự trong lựa chọn size
            setup.add_item()                                                #Thêm
        
        cart = self.get_cart(self.driver) #Quay về cart
        cart.redirect_self()
        self.key_press(Keys.END)
        list_of_item_names = cart.get_list_of_item_names()
        cart.sleep(2)
        
        assert False not in [str(item).lower() in list_of_item_names for item in list(item_list.values())]

    #add mà cùng size giày thì fail
    def test_check_cart_after_add_multi_items(self, setup):
        item_list = {}
        no_items = hp.random_number_in_range(2, 4) #lấy khoản 2 - 4 item

        for i in range(0, no_items):
            setup.redirect_self()                                           #Quay về shop
            rd_item_index = hp.random_number_in_range(1, 8)                 #Lấy só random
            while item_list.get(rd_item_index):
                rd_item_index = hp.random_number_in_range(2, 8)
            
            setup.click_item(rd_item_index)
            current_shoe_name = setup.get_item_name()
            item_list[rd_item_index] = current_shoe_name

            setup.add_item()                                                #Thêm
        
        cart = self.get_cart(self.driver) #Quay về cart
        cart.redirect_self()
        self.key_press(Keys.END)
        list_of_item_names = cart.get_list_of_item_names()
        cart.sleep(2)
        
        assert False not in [str(item).lower() in list_of_item_names for item in list(item_list.values())]

    #như trên
    def test_check_cart_after_add_multi_items_with_random_pages(self, setup):
            
            item_list = {}
            no_items = hp.random_number_in_range(2, 4) #lấy khoản 2 - 4 item

            for i in range(0, no_items):                
                setup.redirect_self()                                            #Quay về shop
                
                random_page = hp.random_number_in_range(0, 5)
                setup.click_next_pages(random_page)                             #Trang random       
                rd_item_index = hp.random_number_in_range(1, 8)                 #Lấy só random
                while item_list.get(rd_item_index):
                    rd_item_index = hp.random_number_in_range(2, 8)
                
                setup.click_item(rd_item_index)
                current_shoe_name = setup.get_item_name()
                item_list[rd_item_index] = current_shoe_name

                setup.add_item()                                                #Thêm
            
            cart = self.get_cart(self.driver) #Quay về cart
            cart.redirect_self()
            self.key_press(Keys.END)
            list_of_item_names = cart.get_list_of_item_names()
            cart.sleep(2)
            
            assert False not in [str(item).lower() in list_of_item_names for item in list(item_list.values())]

    # ===================== Xe hàng =====================#
    def test_cart_summary(self, setup):
        #Thêm sản phẩm
        self.test_add_multi_random_item(setup)
        
        cart = self.get_cart(self.driver)
        cart.redirect_self()
        total = 0
        items_list_elements = self.driver.find_elements(By.XPATH, "//div[@class='cart-item']")
        for element in items_list_elements:
            price = element.find_element(By.XPATH, ".//div[@class='cart-item-right']/p").text
            int_price = cart.int_price(price)
            qty = element.find_element(By.XPATH, ".//div[@class='cart-item-left']/p[3]").text
            int_qty = int(str(qty).split(" ")[1])
            total += int_price*int_qty
        
        
        summary_total = self.driver.find_element(By.XPATH, "//div[@class='cart-summary']//div[@class='space-between bold']/p[2]").text
        summary_total = cart.int_price(summary_total)
        assert total == summary_total

    def test_apply_wrong_discount(self, setup):
        self.test_add_multi_random_item(setup)
        cart = self.get_cart(self.driver)
        cart.redirect_self()

        discount = "100OFF"
        cart.root.input(ElementsPath.CART.DISCOUNT.DISCOUNT_INPUT, f"{discount}")
        cart.root.click(ElementsPath.CART.DISCOUNT.APPLY_BUTTON)
        cart.root.sleep(0.5)
        hp.assert_alert_text_equals(self.driver, "Wrong discount")

    def test_cart_summary_with_discount(self, setup):
        self.test_add_multi_random_item(setup)
        cart = self.get_cart(self.driver)
        cart.redirect_self()

        discount = cart.get_discount_after_apply()

        cart.sleep(1)
        subtotal = cart.int_price(self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[2]/div[1]/div[1]/p[2]").text)
        
        total = cart.int_price(self.driver.find_element(By.XPATH, "//div[@class='cart-summary']//div[@class='space-between bold']/p[2]").text)
        
        calculate = subtotal - (subtotal*discount)/100
        assert total == calculate

    def test_change_qty(self, setup):
        self.test_add_multi_random_item(setup)
        cart = self.get_cart(self.driver)
        cart.redirect_self()
        
        current_total = cart.int_price(self.driver.find_element(By.XPATH, "//div[@class='cart-summary']//div[@class='space-between bold']/p[2]").text)
        
        #Kiểm gia tăng số lượng
        item_price = cart.int_price(self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[1]/div/div[1]/div/div[2]/p").text)
        increase_btn = self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[1]/div/div[1]/div/div[2]/div/a[2]")
        increase_btn.click()
        
        cart.sleep(2)
        new_total = cart.int_price(self.driver.find_element(By.XPATH, "//div[@class='cart-summary']//div[@class='space-between bold']/p[2]").text)

        assert new_total == current_total + item_price # Kiểm tra sau khi tăng gì giá total như lào

        decrease_btn = self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[1]/div/div[1]/div/div[2]/div/a[1]")
        decrease_btn.click()
        cart.sleep(2)
        new_total = cart.int_price(self.driver.find_element(By.XPATH, "//div[@class='cart-summary']//div[@class='space-between bold']/p[2]").text)

        assert current_total == new_total #Kiểm tra sau khi giảm

    def test_remove(self, setup):
        self.test_add_multi_random_item(setup)
        cart = self.get_cart(self.driver)
        cart.redirect_self()

        items_list_elements = self.driver.find_elements(By.XPATH, "//div[@class='cart-item']")
        rd_index = hp.random_number_in_range(0, len(items_list_elements)-1)
        item = items_list_elements[rd_index]

        item_price = cart.int_price(item.find_element(By.XPATH, ".//div[@class='cart-item-right']/p").text)
        qty = item.find_element(By.XPATH, ".//div[@class='cart-item-left']/p[3]").text
        int_qty = int(str(qty).split(" ")[1])
        remove_item_name = item.find_element(By.XPATH, ".//div[@class='cart-item-left']//a[1]").text
        current_total = cart.int_price(self.driver.find_element(By.XPATH, "//div[@class='cart-summary']//div[@class='space-between bold']/p[2]").text)

        remove_btn = item.find_element(By.XPATH, ".//div[@class='cart-item-left']//a[2]")
        remove_btn.click()
        cart.sleep(2)

        new_total = cart.int_price(self.driver.find_element(By.XPATH, "//div[@class='cart-summary']//div[@class='space-between bold']/p[2]").text)
        assert new_total == current_total - (item_price*int_qty)

        items_list_elements = self.driver.find_elements(By.XPATH, "//div[@class='cart-item']")
        for item in items_list_elements:
            assert remove_item_name not in item.find_element(By.XPATH, ".//div[@class='cart-item-left']//a[1]").text
    
    def test_empty_cart(self, setup_cart):

        # self.key_press(Keys.END)

        items_list_elements = self.driver.find_elements(By.XPATH, "//div[@class='cart-item']")
        for item in items_list_elements:
            remove_btn = item.find_element(By.XPATH, ".//div[@class='cart-item-left']//a[2]")
            remove_btn.click()

        setup_cart.sleep(1)
        assert setup_cart.root.text(ElementsPath.CART.IS_EMPTY.TEXT_PATH) == ElementsPath.CART.IS_EMPTY.TEXT

    # ===================== Checkout =====================#
    #fail vì không bấm nút paypal được
    def test_checkout(self, setup_cart):

        checkout_btn = self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[2]/div[1]/a/button")
        checkout_btn.click()
        setup_cart.sleep(0.5)

        shipping_next_btn = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/a[2]/button")
        shipping_next_btn.click()
        setup_cart.sleep(0.5)

        payment_next_btn = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/a[2]/button")
        payment_next_btn.click()
        setup_cart.sleep(0.5)

        #paypal;
        paypal_btn = self.get_clickable_element(self.driver, By.XPATH, "//span[text()=' Checkout']")
        paypal_btn.click()
        setup_cart.sleep(2)
    
    def test_apply_discount_in_checkout(self, setup_cart):
        checkout_btn = self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[2]/div[1]/a/button")
        checkout_btn.click()
        setup_cart.sleep(0.5)

        shipping_next_btn = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/a[2]/button")
        shipping_next_btn.click()
        setup_cart.sleep(0.5)

        payment_next_btn = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/a[2]/button")
        payment_next_btn.click()
        setup_cart.sleep(0.5)

        current_total = setup_cart.int_price(self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[2]/div[3]/div[4]/p[2]").text)

        self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[2]/div[2]/input").send_keys("10OFF")
        apply_btn = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[2]/div[2]/button")
        apply_btn.click()
        setup_cart.sleep(2)

        new_total = setup_cart.int_price(self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[2]/div[2]/div[5]/p[2]").text)
        
        assert current_total - (current_total *10)/100 == new_total

    def test_remove_all_item_in_checkout(self, setup_cart):
        checkout_btn = self.driver.find_element(By.XPATH, "//*[@id='root']/div[1]/div[2]/div[1]/a/button")
        checkout_btn.click()
        setup_cart.sleep(0.5)

        shipping_next_btn = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/a[2]/button")
        shipping_next_btn.click()
        setup_cart.sleep(0.5)

        payment_next_btn = self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[2]/a[2]/button")
        payment_next_btn.click()
        setup_cart.sleep(0.5)

        remove_elements = self.driver.find_elements(By.XPATH, "//div[@class='cart-item-left']//a[2]")
        for remove in remove_elements:
            remove.click()
        
        
        assert "0" in self.driver.find_element(By.XPATH, "//*[@id='root']/div/div/div[1]/div/div[2]/div[3]/div[4]/p[2]").text



    
