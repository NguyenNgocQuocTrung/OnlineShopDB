import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def test_search_single_keyword():
    driver = webdriver.Edge()
    driver.get("https://ktpm.nguyenngocquoctrung.id.vn/shop")
    time.sleep(2)

    search_box = driver.find_element(By.ID, "search")
    search_box.send_keys("a")
    time.sleep(1)

    # Lấy danh sách các sản phẩm
    product_grid = driver.find_elements(By.CSS_SELECTOR, "div.product-grid > div.product-card") 
    
    # Kiểm tra xem có sản phẩm xuất hiện trong kết quả không
    assert len(product_grid) > 0, "Không có sản phẩm nào được tìm thấy."
    driver.quit()

def test_search_full_keyword():
    driver = webdriver.Edge()
    driver.get("https://ktpm.nguyenngocquoctrung.id.vn/shop")
    time.sleep(2)

    search_box = driver.find_element(By.ID, "search")
    search_box.send_keys("Nike")
    time.sleep(1)
    
    # Lấy danh sách các sản phẩm
    product_grid = driver.find_elements(By.CSS_SELECTOR, "div.product-grid > div.product-card")
    
    # Kiểm tra xem có sản phẩm xuất hiện trong kết quả không
    assert len(product_grid) > 0, "Không có sản phẩm nào được tìm thấy với từ khóa đầy đủ."
    driver.quit()

def test_delete_keyword():
    driver = webdriver.Edge()
    driver.get("https://ktpm.nguyenngocquoctrung.id.vn/shop")
    time.sleep(2)

    search_box = driver.find_element(By.ID, "search")
    search_term = 'adidas questar flow nxt "core black"'
    search_box.send_keys(search_term)
    time.sleep(1)
    
    # Lấy danh sách các sản phẩm sau khi nhập từ khóa tìm kiếm
    initial_product_count = len(driver.find_elements(By.CSS_SELECTOR, "div.product-grid > div.product-card"))

    # Xóa từng ký tự
    for i in range(len(search_term)):
        search_box.send_keys(Keys.BACKSPACE)
        time.sleep(0.5)

        # Lấy số lượng sản phẩm sau khi xóa một ký tự
        current_product_count = len(driver.find_elements(By.CSS_SELECTOR, "div.product-grid > div.product-card"))
        
        # Kiểm tra số lượng sản phẩm có thay đổi không
        if current_product_count != initial_product_count:
            print(f"Test thành công: Sau khi xóa đến ký tự thứ {i+1}, số lượng sản phẩm đã thay đổi từ {initial_product_count} đến {current_product_count}.")
            break
    
    assert current_product_count != initial_product_count, "Số lượng sản phẩm không thay đổi sau khi xóa ký tự."
    driver.quit()

def test_search_non_existent_keyword():
    driver = webdriver.Edge()  # Khởi tạo WebDriver, ví dụ: Edge
    driver.get("https://ktpm.nguyenngocquoctrung.id.vn/shop")  # URL trang web demo
    time.sleep(2)

    search_box = driver.find_element(By.ID, "search")
    search_term = "xyz"
    search_box.send_keys(search_term)
    time.sleep(1)

    # Lấy danh sách các sản phẩm
    product_grid = driver.find_elements(By.CSS_SELECTOR, "div.product-grid > div.product-card")
    
    # Kiểm tra số lượng sản phẩm
    assert len(product_grid) == 0, f"Tìm thấy sản phẩm với từ khóa '{search_term}'."
    driver.quit()

def test_search_empty_keyword():
    driver = webdriver.Edge()  # Khởi tạo WebDriver, ví dụ: Edge
    driver.get("https://ktpm.nguyenngocquoctrung.id.vn/shop")  # URL trang web demo
    time.sleep(2)

    search_box = driver.find_element(By.ID, "search")
    search_box.clear() 
    search_box.send_keys("")
    time.sleep(1)

    # Lấy danh sách các sản phẩm
    product_grid = driver.find_elements(By.CSS_SELECTOR, "div.product-grid > div.product-card")
    
    # Kiểm tra tất cả sản phẩm đều xuất hiện
    assert len(product_grid) > 0, "Không có sản phẩm nào được hiển thị khi tìm kiếm với từ khóa rỗng."
    driver.quit()

def test_search_special_characters():
    driver = webdriver.Edge()
    driver.get("https://ktpm.nguyenngocquoctrung.id.vn/shop")
    time.sleep(2)

    search_box = driver.find_element(By.ID, "search")
    search_term = "!@#!@%&**♥♣"
    search_box.send_keys(search_term)
    time.sleep(1)

    # Lấy danh sách các sản phẩm
    product_grid = driver.find_elements(By.CSS_SELECTOR, "div.product-grid > div.product-card") 
    
    # Kiểm tra xem có sản phẩm xuất hiện trong kết quả không
    assert len(product_grid) == 0, f"Tìm thấy sản phẩm với từ khóa '{search_term}'."
    driver.quit()

def test_search_long_string():
    driver = webdriver.Edge()  # Khởi tạo WebDriver, ví dụ: Edge
    driver.get("https://ktpm.nguyenngocquoctrung.id.vn/shop")  # URL trang web demo
    time.sleep(2)

    search_box = driver.find_element(By.ID, "search")
    long_search_term = "adidas " * 100 
    search_box.send_keys(long_search_term)
    time.sleep(3)

    # Lấy danh sách các sản phẩm
    product_grid = driver.find_elements(By.CSS_SELECTOR, "div.product-grid > div.product-card")
    
    # Kiểm tra xem có sản phẩm xuất hiện trong kết quả không
    assert len(product_grid) == 0, "Có sản phẩm nào được tìm thấy khi tìm kiếm với chuỗi rất dài."
    driver.quit()

def test_search_with_whitespace():
    driver = webdriver.Edge()
    driver.get("https://ktpm.nguyenngocquoctrung.id.vn/shop")
    time.sleep(2)

    search_box = driver.find_element(By.ID, "search")
    search_box.send_keys("  nike air max 270  ")
    time.sleep(1)
    
    # Lấy danh sách các sản phẩm
    product_grid = driver.find_elements(By.CSS_SELECTOR, "div.product-grid > div.product-card")
    
    # Kiểm tra xem có sản phẩm xuất hiện trong kết quả không
    assert len(product_grid) == 0, "Tìm thấy sản phẩm với từ khóa có khoảng trắng."
    driver.quit()