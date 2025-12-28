import pytest
from selenium import webdriver

@pytest.fixture()
def browser():
   browser=webdriver.Chrome()
   browser.maximize_window()
   browser.implicitly_wait(10)
   yield browser
   input("Нажмите Enter, чтобы закрыть браузер...")
   browser.quit()
   