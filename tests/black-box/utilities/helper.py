import random
import string
import time
from constants import config as cf
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#region: Randoms
def random_string_and_digits(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def random_string(length):
    characters = string.ascii_letters
    return ''.join(random.choice(characters) for _ in range(length))

def random_digits_len(length):
    characters = string.digits
    return ''.join(random.choice(characters) for _ in range(length))

def random_number_in_range(min_value, max_value):
    return random.randint(min_value, max_value)

def random_string_with_space(length):
    characters = string.ascii_letters + " "
    return ''.join(random.choice(characters) for _ in range(length))



#region: Assertions 
def assert_alert_text_equals(driver, text):
    time.sleep(0.1)
    alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
    alert_text = alert.text
    assert alert_text == text
    alert.accept()

def assert_current_url_equals_account_url(driver):
    time.sleep(0.1)
    url = cf.BASE_URL + cf.ACCOUNT_ENDPOINT
    assert driver.current_url == url

def assert_error_messsages_equals( root, expected_messages):
    time.sleep(0.1)
    actual_message = root.get_error_messages()
    time.sleep(0.1)
    assert actual_message == expected_messages

def assert_text_in_src_page(driver,txt):
    time.sleep(0.1)
    assert txt in driver.page_source

def assert_text_in_message(root, root_element, text):
    time.sleep(0.1)
    message = root.get_text(root_element)
    assert text in message
