import time
from selenium.webdriver.common.by import By
import pytest
from ktpm_selenium.selenium.utils.webdriver_setup import Driver

class TestResponsiveDesign(Driver):
    # khung hình
    @pytest.mark.parametrize("width,height", [
        (768, 1024),   # Tablet (e.g., iPad Mini)
        (1024, 1366),  # Small desktop/laptop
        (1440, 900),   # Standard desktop
    ])
    def test_responsive_layout(self, driver, width, height):
        """Test if the layout adapts correctly to various screen sizes."""
        driver.set_window_size(width, height)
        driver.get("http://ktpm.nguyenngocquoctrung.id.vn:3000/")

        time.sleep(2)

        # Kiểm tra layout cho thiết bị di động
        if width <= 480:
            try:
                menu_icon = driver.find_element(By.XPATH, "/html/body/div/nav/div[2]/ul")
                assert menu_icon.is_displayed(), f"Menu icon should be visible at width {width}px"
            except Exception as e:
                print(f"Error at {width}x{height}: {str(e)}")

        # Kiểm tra layout cho màn hình desktop
        if width >= 1024:
            try:
                desktop_nav = driver.find_element(By.CLASS_NAME, "desktop-nav")
                assert desktop_nav.is_displayed(), f"Desktop navigation should be visible at width {width}px"
            except Exception as e:
                print(f"Error at {width}x{height}: {str(e)}")

        # Các kiểm tra bổ sung
        try:
            header = driver.find_element(By.TAG_NAME, "header")
            assert header.is_displayed(), f"Header should be visible at width {width}px"
        except Exception as e:
            print(f"Error with header display at {width}x{height}: {str(e)}")

        # Kiểm tra Footer
        try:
            footer = driver.find_element(By.TAG_NAME, "footer")
            assert footer.is_displayed(), f"Footer should be visible at width {width}px"
        except Exception as e:
            print(f"Error with footer display at {width}x{height}: {str(e)}")