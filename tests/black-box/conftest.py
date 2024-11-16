import pytest
from selenium import webdriver
from constants.elements_path import ElementsPath
from constants import config

@pytest.fixture(autouse=True)
def driver():
  if config.BROWSER == "edge":
    try:
      driver = webdriver.Edge()
    except: driver = webdriver.Chrome()
  else: driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get(config.BASE_URL)
  yield driver
  driver.quit()

# @pytest.fixture(scope="class",autouse=True)
# def elements_path(driver):
#   return ElementsPath(driver) 

