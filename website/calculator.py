from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class calculator:
    def __init__(self,browser):
        self.browser=browser
        
    def open(self):
        self.browser.get("https://calculator.megamarket.ru/")
        
    def choose_goods(self):
        element = self.browser.find_element(By.NAME, "search")
        element.clear()
        element= element.send_keys("стол")
        search_button = self.browser.find_element(By.CSS_SELECTOR, "button.smm-input__button_after-icon")
        search_button.click()  
        
        select_good = self.browser.find_element(By.CSS_SELECTOR, "li.calculator-product-search-item[data-pickable='true']")
        select_good.click()         
    