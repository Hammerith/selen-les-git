from selenium import webdriver
import math
import time


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/math.html')
    x = browser.find_element_by_css_selector('[id = "input_value"]').text
    browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(math.log(abs(12*math.sin(int(x))))))
    # check = browser.find_element_by_id('robotCheckbox')
    # check.click()
    # radio_btn = browser.find_element_by_id('robotsRule')
    # radio_btn.click()
    # submit_btn = browser.find_element_by_css_selector('button.btn.btn-default')
    # submit_btn.click()
    for selector in ['[for = "robotCheckbox"]', '[for = "robotsRule"]', '.btn']:
        browser.find_element_by_css_selector(selector).click()

finally:
    time.sleep(7)
    browser.quit()

