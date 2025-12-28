import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def browser():
   browser=Options()
   browser=webdriver.Firefox(options=browser)
   browser.implicitly_wait(10)
   yield browser
   browser.quit()
   

