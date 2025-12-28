from selenium.webdriver.firefox.webdriver import WebDriver
from website.calculator import calculator
   
def test_open_site(browser):
   Сalculator=calculator(browser)
   Сalculator.open()
   Сalculator.choose_goods()