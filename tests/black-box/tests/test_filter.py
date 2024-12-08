from itertools import product
import json
import time
from tkinter.tix import Select
import pytest
from selenium.webdriver.common.by import By

from pages.authentication_page import LoginPage
from constants.elements_path import ElementsPath
from utilities import helper as hp
from pages.filter_page import FilterPage

class TestFilter:   
    @pytest.fixture(autouse=True)
    def setup(self,driver):
        shop_page = FilterPage(driver)
        shop_page.redirect_self()
        return shop_page

        
    # def test_filter_by_price(self, driver):
    #     # Tìm input cho Min và Max giá
    #     time.sleep(3)
    #     filter_box = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div[1]/div[1]/div[1]/a")
    #     filter_box.click()
        
    #     min_price_input = driver.find_element(By.XPATH, "//*[@id=\"minPrice\"]")
    #     max_price_input = driver.find_element(By.XPATH, "//*[@id=\"maxPrice\"]")
        
    #     time.sleep(3)
    #     # Nhập giá trị min và max vào các trường input
    #     min_price_input.clear()
    #     min_price_input.send_keys("3000000")  # Giá min
    #     max_price_input.clear()
    #     max_price_input.send_keys("3200000")  # Giá max

    #     time.sleep(3)

    #    # Lấy tất cả các sản phẩm
    #     product_cards = driver.find_elements(By.XPATH, "//*[@class='product-card']")
        
    #     # Lấy giá sản phẩm từ mỗi sản phẩm
    #     for card in product_cards:
    #         # Lấy giá sản phẩm trong thẻ p (product-info)
    #         price_text = card.find_element(By.XPATH, "//*[@id=\"root\"]/div[1]/div[2]/div[1]/div[2]/a/p[2]").text
            
    #        # 1. Loại bỏ tất cả khoảng trắng thừa và ký tự HTML không cần thiết (ví dụ: "&nbsp;")
    #         price_text = price_text.replace("&nbsp;", "").strip()

    #         # 2. Loại bỏ dấu phân cách nghìn (dấu chấm) và ký tự tiền tệ "kr."
    #         price_text = price_text.replace(".", "")  # Loại bỏ dấu phân cách nghìn
    #         price_text = price_text.replace("kr", "").strip()  # Loại bỏ ký tự tiền tệ "kr."
    #         price_text = price_text.replace(",00", "")  # Loại bỏ dấu phân cách nghìn
            

    #         # 4. Chuyển đổi thành float
    #         try:
    #             price = int(price_text)
    #             print(f"Converted price: {price}")
    #         except ValueError as e:
    #             print(f"Error converting price: {e}")
            
    #         # Assert rằng giá của mỗi sản phẩm phải nằm trong khoảng min và max
    #         assert 3000000 <= price <= 3200000, f"Price {price} is outside the range."

    #     # In kết quả để kiểm tra
    #     print(f"Products within the price range 100000 - 500000: {len(product_cards)}")
               
    # def test_filter_by_out_price(self, driver):
    #     # Tìm input cho Min và Max giá
    #     time.sleep(3)
    #     filter_box = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div[1]/div[1]/div[1]/a")
    #     filter_box.click()
        
    #     min_price_input = driver.find_element(By.XPATH, "//*[@id=\"minPrice\"]")
    #     max_price_input = driver.find_element(By.XPATH, "//*[@id=\"maxPrice\"]")
        
    #     time.sleep(3)
    #     # Nhập giá trị min và max vào các trường input
    #     min_price_input.clear()
    #     min_price_input.send_keys("5000000")  # Giá min
    #     max_price_input.clear()
    #     max_price_input.send_keys("6000000")  # Giá max

    #     time.sleep(3)
        
    #     product_cards = driver.find_elements(By.XPATH, "//*[@class='product-card']")
        
    #     assert len(product_cards) == 0, "There are products displayed for price you selected, but there should be none."
        
    # def test_filter_by_lowest_to_highest(self, driver):
    #     # Tìm input cho Min và Max giá
    #     time.sleep(3)
    #     filter_box = driver.find_element(By.XPATH, "//*[@id=\"root\"]/div[1]/div[1]/div[1]/a")
    #     filter_box.click()
        
    #     sort = driver.find_element(By.XPATH, "//*[@id=\"sort\"]")
    #     sort.click()
        
    #     time.sleep(1)
    #     sort_by_lowest_to_highest = sort.find_element(By.XPATH, "//*[@id=\"sort\"]/option[2]")  
    #     sort_by_lowest_to_highest.click()
    #     time.sleep(3)
        
        
    #         # Lấy tất cả các product-card trong product-grid
    #     product_cards = driver.find_elements(By.XPATH, '//*[@class="product-card"]')
        
    #     # Lấy giá của tất cả các sản phẩm trong mỗi product-card
    #     prices = []
    #     for card in product_cards:
    #         # Lấy giá sản phẩm trong product-info
    #         price_text = card.find_elements(By.XPATH, ".//div[@class='product-info']/p").text
    #         # Làm sạch giá, loại bỏ dấu phân cách và ký tự tiền tệ
    #         # 1. Loại bỏ tất cả khoảng trắng thừa và ký tự HTML không cần thiết (ví dụ: "&nbsp;")
    #         price_text = price_text.replace("&nbsp;", "").strip()

    #         # 2. Loại bỏ dấu phân cách nghìn (dấu chấm) và ký tự tiền tệ "kr."
    #         price_text = price_text.replace(".", "")  # Loại bỏ dấu phân cách nghìn
    #         price_text = price_text.replace("kr", "").strip()  # Loại bỏ ký tự tiền tệ "kr."
    #         price_text = price_text.replace(",00", "")  # Loại bỏ dấu phân cách nghìn
    #         price = int(price_text)
    #         prices.append(price)
        
    #     # Kiểm tra xem các giá có được sắp xếp theo thứ tự giảm dần không
    #     assert prices == sorted(prices, reverse=True), f"Prices are not sorted correctly: {prices}"



    def test_filter_by_size(self, setup):
        """
        Kiểm tra bộ lọc sản phẩm theo kích cỡ.
        """
        # Bước 1: Áp dụng bộ lọc
        setup.apply_filter()

        # Bước 2: Chọn kích cỡ ngẫu nhiên
        selected_size = setup.select_random_size(1,9)
        # Bước 3: Kiểm tra các sản phẩm hiển thị khớp với kích cỡ đã chọn
        setup.select_product()
        product_sizes = setup.get_product_sizes()

        assert selected_size in product_sizes, f"Sản phẩm có kích cỡ {selected_size} không khớp với kích cỡ {product_sizes}."
        
    def test_filter_by_no_size(self, setup):
        """
        Kiểm tra bộ lọc sản phẩm không có kích cỡ.
        """
        # Bước 1: Áp dụng bộ lọc
        setup.apply_filter()

        # Bước 2: Chọn kích cỡ ngẫu nhiên
        setup.select_random_size(10,15)
        
        product_sizes = setup.get_product_list()

        assert len(product_sizes) == 0, "There are products displayed for size you selected, but there should be none."
        
    
    def test_filter_by_price(self, setup):
        """
        Kiểm tra bộ lọc sản phẩm theo giá.
        """
        # Bước 1: Áp dụng bộ lọc
        setup.apply_filter()
        min_price = 3000000
        max_price = 3200000

        # Bước 2: Nhập giá trị min và max
        setup.set_price_filter(min_price, max_price)

        product_prices = setup.get_product_prices()

        # Bước 3: Kiểm tra tất cả các sản phẩm có giá trong khoảng từ min_price đến max_price
        for price in product_prices:
            assert 3000000 <= price <= 3200000, f"Price {price} is outside the range."
        
    def test_filter_by_out_price(self, setup):
            
        """
        Kiểm tra bộ lọc sản phẩm theo giá.
        """
        # Bước 1: Áp dụng bộ lọc
        setup.apply_filter()
        min_price = 5000000
        max_price = 6000000

        # Bước 2: Nhập giá trị min và max
        setup.set_price_filter(min_price, max_price)

        product_prices = setup.get_product_prices()

        assert len(product_prices) == 0, "There are products displayed for price you selected, but there should be none."
        
        
    def test_filter_by_lowest_to_highest(self, setup):
        """
        Kiểm tra bộ lọc sản phẩm theo giá.
        """
        # Bước 1: Áp dụng bộ lọc
        setup.apply_filter()
        setup.sort_by_lowest_to_highest()

        # Bước 2: Lấy giá của tất cả các sản phẩm sau khi sắp xếp
        product_cards = setup.get_all_products()
        product_price = setup.get_all_product_prices(product_cards)
        
        assert product_price == sorted(product_price), f"Prices are not sorted correctly: {product_price}"
            
            
    def test_filter_by_highest_to_lowest(self, setup):
        """
        Kiểm tra bộ lọc sản phẩm theo giá.
        """
        # Bước 1: Áp dụng bộ lọc
        setup.apply_filter()
        setup.sort_by_highest_to_lowest()

        # Bước 2: Lấy giá của tất cả các sản phẩm sau khi sắp xếp
        product_cards = setup.get_all_products()
        product_price = setup.get_all_product_prices(product_cards)
        
        assert product_price == sorted(product_price, reverse=True), f"Prices are not sorted correctly: {product_price}"
        
    
    def test_filter_by_lowest_to_highest_with_size(self, setup):
        """
        Kiểm tra bộ lọc sản phẩm theo giá và kích cỡ.
        """
        # Bước 1: Áp dụng bộ lọc
        setup.apply_filter()
        setup.sort_by_lowest_to_highest()
        selected_size = setup.select_random_size(1,9)
        
        setup.select_product()
        product_sizes = setup.get_product_sizes()
        
        assert selected_size in product_sizes, f"Sản phẩm có kích cỡ {selected_size} không khớp với kích cỡ {product_sizes}."
        
        
    def test_filter_by_lowest_to_highest_with_no_size(self, setup):
        """
        Kiểm tra bộ lọc sản phẩm theo giá và kích cỡ.
        """
        # Bước 1: Áp dụng bộ lọc
        setup.apply_filter()
        setup.sort_by_lowest_to_highest()
        selected_size = setup.select_random_size(10,15)
        product_sizes = setup.get_product_list()
        
        assert len(product_sizes) == 0, "There are products displayed for size you selected, but there should be none."

        
    def test_filter_by_highest_to_lowest_with_size(self, setup):
        """
        Kiểm tra bộ lọc sản phẩm theo giá và kích cỡ.
        """
        # Bước 1: Áp dụng bộ lọc
        setup.apply_filter()
        setup.sort_by_highest_to_lowest()
        selected_size = setup.select_random_size(1,9)
        
        setup.select_product()
        product_sizes = setup.get_product_sizes()
        
        assert selected_size in product_sizes, f"Sản phẩm có kích cỡ {selected_size} không khớp với kích cỡ {product_sizes}."
        
        
    def test_filter_by_highest_to_lowest_with_no_size(self, setup):
        """
        Kiểm tra bộ lọc sản phẩm theo giá và kích cỡ.
        """
        # Bước 1: Áp dụng bộ lọc
        setup.apply_filter()
        setup.sort_by_highest_to_lowest()
        selected_size = setup.select_random_size(10,15)
        product_sizes = setup.get_product_list()
        
        assert len(product_sizes) == 0, "There are products displayed for size you selected, but there should be none."