from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/selects1.html')
    result = str(int(browser.find_element_by_css_selector('[id = "num1"]').text) + \
             int(browser.find_element_by_css_selector('[id = "num2"]').text))
    select = Select(browser.find_element_by_css_selector("select"))
    select.select_by_value(result)
    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(7)
    browser.quit()