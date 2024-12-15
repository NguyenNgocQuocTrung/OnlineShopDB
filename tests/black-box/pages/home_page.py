import time

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    # go to home page
    def go_to_home_page(self):
        self.driver.get("http://ktpm.nguyenngocquoctrung.id.vn:3000/")
        time.sleep(3)
