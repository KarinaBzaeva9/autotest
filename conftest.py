import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def browser():
   browser=Options()
   browser.add_argument("--headless") 
   browser.add_argument("--no-sandbox")
   browser.add_argument("--disable-dev-shm-usage")
   browser=webdriver.Firefox(options=browser)
   browser.implicitly_wait(10)
   yield browser
   browser.quit()
   