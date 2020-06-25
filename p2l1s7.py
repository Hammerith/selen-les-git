from selenium import webdriver
from math import log, sin
import time


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/get_attribute.html')
    chest = browser.find_element_by_css_selector('[id = "treasure"]')
    x = int(chest.get_attribute('valuex'))
    browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12*sin(x)))))
    for selector in ['[id = "robotCheckbox"]', '[id = "robotsRule"]', '.btn']:
        browser.find_element_by_css_selector(selector).click()

finally:
    time.sleep(7)
    browser.quit()
