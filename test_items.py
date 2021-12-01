import time
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_add_to_cart_button_is_displayed(browser):
    browser.get(link)
    time.sleep(5)
    try:
        element = browser.find_element(By.XPATH, '//*[contains(@class,"btn-add-to-basket")]')
        #element = browser.find_element(By.XPATH, '//*[contains(@class,"btn-add-to-add")]')
    except NoSuchElementException:
        assert False, "No Such Element"
