import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture()
def browser():
   browser=Options()
   browser.add_argument("--headless") 
   browser.add_argument("--no-sandbox")
   browser.add_argument("--disable-dev-shm-usage")
   browser.set_preference("browser.tabs.remote.autostart", False)
   browser.set_preference("browser.tabs.remote.autostart.1", False)
   browser.set_preference("browser.tabs.remote.autostart.2", False)
   browser=webdriver.Firefox(options=browser)
   browser.implicitly_wait(10)
   yield browser
   browser.quit()
   

