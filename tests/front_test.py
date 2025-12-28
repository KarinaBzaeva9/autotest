from website.calculator import calculator
   
def test_opet_site(browser):
   Сalculator=calculator(browser)
   Сalculator.open()
   Сalculator.choose_goods()