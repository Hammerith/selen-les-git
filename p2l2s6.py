from selenium import webdriver
import time
from math import log, sin

try:
    browser = webdriver.Chrome()
    browser.get("https://SunInJuly.github.io/execute_script.html")
    field = browser.find_element_by_css_selector('[id = "answer"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", field)
    x = int(browser.find_element_by_css_selector("[id = 'input_value']").text)
    field.send_keys(str(log(abs(12*sin(x)))))
    for selector in ['[id = "robotCheckbox"]', '[id = "robotsRule"]', '.btn']:
        browser.find_element_by_css_selector(selector).click()

finally:
    time.sleep(5)
    browser.quit()