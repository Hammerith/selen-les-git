from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from math import log, sin
import time
import pyperclip
import pickle


try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/explicit_wait2.html')
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100')
    )
    browser.find_element_by_css_selector('[id = "book"]').click()
    x = int(browser.find_element_by_css_selector('[id = "input_value"]').text)
    browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12*sin(x)))))
    browser.find_element_by_css_selector('[id = "solve"]').click()
    alert = browser.switch_to.alert
    alert_text = alert.text.split(': ')[-1]
    pyperclip.copy(alert_text)
    alert.accept()
    browser.implicitly_wait(5)
    browser.get('https://stepik.org')
    cookies = pickle.load(open('cookies.pkl', 'rb'))
    for cookie in cookies:
        browser.add_cookie(cookie)
    browser.refresh()
    browser.implicitly_wait(5)
    browser.get('https://stepik.org/lesson/181384/step/8?unit=156009')
    browser.find_element_by_class_name('textarea').send_keys(pyperclip.paste())
    browser.find_element_by_css_selector('[class = "submit-submission"]').click()
finally:
    time.sleep(5)
    browser.quit()