import json
import random
from time import sleep

from websocket import send
from constants.filter_elements_path import FilterElementsPath
from constants.elements_path import ElementsPath
from selenium.webdriver.common.by import By
from utilities import helper as hp



class FilterPage:
    def __init__(self, driver):
        self.driver = driver
        self.root = FilterElementsPath(driver)
        
    def redirect_self(self):
        self.root.click(ElementsPath.NAVIGATION.SHOP)
        
    def apply_filter(self):
        self.root.click(FilterElementsPath.FILTER.FILTER_BOX)

    def select_random_size(self, min_size, max_size):
        # Click vào hộp size
        self.root.click(FilterElementsPath.FILTER.SIZE_BOX)

        # Lấy danh sách các option
        options = self.root.elements_name(FilterElementsPath.FILTER.OPTION)
        size_options = [option for option in options if option.get_attribute(FilterElementsPath.FILTER.VALUE) != 'all']

        # Kiểm tra danh sách không rỗng
        if size_options:
            # Chọn ngẫu nhiên một size trong phạm vi từ min_size đến max_size
            random_index = hp.random_number_in_range(min_size, max_size)  # Chỉ số ngẫu nhiên trong phạm vi được chỉ định
            selected_size = size_options[random_index]  # Trừ 1 vì chỉ số bắt đầu từ 1
            selected_size.click()
            return selected_size.get_attribute(FilterElementsPath.FILTER.VALUE)
        return None


    def select_product(self):
        # Click vào sản phẩm
        self.root.click(FilterElementsPath.FILTER.PRODUCT)

    def get_product_sizes(self):
        # Kiểm tra xem có sản phẩm hay không
        # product_list = self.root.elements_name(FilterElementsPath.FILTER.PRODUCT)
        # if not product_list:
        #     print("No products found.")
        #     return []  # Nếu không có sản phẩm, trả về danh sách rỗng
        
        # Nếu có sản phẩm, thực hiện các thao tác lấy kích cỡ
        self.root.click(FilterElementsPath.FILTER.PRODUCT_SIZE_BOX)
        
        # Lấy các option size của sản phẩm
        options = self.root.elements_name(FilterElementsPath.FILTER.OPTION)
        product_sizes = []
        
        for option in options:
            value = option.get_attribute(FilterElementsPath.FILTER.VALUE)
            if value:
                try:
                    json_data = json.loads(value.replace('&quot;', '"'))
                    product_sizes.append(str(json_data.get('size')))
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON: {e}")
        
        return product_sizes

    def get_product_list(self):
        # Kiểm tra xem có sản phẩm hay không
        product_list = self.root.elements_name(FilterElementsPath.FILTER.PRODUCT)
        if not product_list:
            print("No products found.")
            return []  # Nếu không có sản phẩm, trả về danh sách rỗng

    def send_keys_min_price(self, min_price):
        min_price_input = self.root.element(FilterElementsPath.FILTER.MIN_PRICE)
        min_price_input.send_keys(min_price)
        
    def send_keys_max_price(self, max_price):
        max_price_input = self.root.element(FilterElementsPath.FILTER.MAX_PRICE)
        max_price_input.send_keys(max_price)
        
    def set_price_filter(self, min_price, max_price):
        """
        Nhập giá trị vào các trường Min và Max Price để lọc sản phẩm.
        """
        self.send_keys_min_price(min_price)
        sleep(3)
        self.send_keys_max_price(max_price)

    def remove_price_text(self, price_text):
        price_text = price_text.replace("&nbsp;", "").strip()
        price_text = price_text.replace(".", "").replace("kr", "").strip()
        return price_text
    

    # Hàm chọn bộ lọc sắp xếp "Lowest to Highest"
    def sort_by_lowest_to_highest(self):
        sort_dropdown = self.root.element(FilterElementsPath.FILTER.SORT)
        sort_dropdown.click()
        
        sort_option = self.root.element(FilterElementsPath.FILTER.SORT_BY_LOWEST_TO_HIGHEST)
        sort_option.click()
    
    def sort_by_highest_to_lowest(self):
        sort_dropdown = self.root.element(FilterElementsPath.FILTER.SORT)
        sort_dropdown.click()
        
        sort_option = self.root.element(FilterElementsPath.FILTER.SORT_BY_HIGHEST_TO_LOWEST)
        sort_option.click()

    # Hàm lấy tất cả các sản phẩm trên trang
    def get_all_products(self):
        product_cards = self.root.elements(FilterElementsPath.FILTER.PRODUCT_CARD)
        return product_cards

    # Hàm lấy giá của sản phẩm
    def get_all_product_prices(self, product_cards):
        prices = []
        for card in product_cards:
            # Lấy tất cả các phần tử chứa giá trong một sản phẩm (nếu có nhiều giá)
            price_elements = card.find_elements(By.XPATH, FilterElementsPath.FILTER.PRODUCT_PRICE)
            
            for price_element in price_elements:
                price_text = price_element.text.strip()
                
                # Làm sạch giá trị
                price_text = price_text.replace("&nbsp;", "").replace(".", "").replace("kr", "").replace(",00", "").strip()
                
                try:
                    price = int(price_text)
                    prices.append(price)
                except ValueError:
                    continue  # Bỏ qua nếu không thể chuyển giá trị thành số
        return prices
