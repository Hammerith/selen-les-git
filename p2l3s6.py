from selenium import webdriver
import time
import pyperclip
from math import log, sin
import pickle

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/redirect_accept.html')
    browser.find_element_by_css_selector('.btn').click()
    next_tab = browser.window_handles[1]
    browser.switch_to.window(next_tab)
    x = int(browser.find_element_by_css_selector('[id = "input_value"]').text)
    browser.find_element_by_css_selector('[id = "answer"]').send_keys(str(log(abs(12*sin(x)))))
    browser.find_element_by_css_selector('.btn').click()
    alert = browser.switch_to.alert
    alert_text = alert.text.split(': ')[-1]
    pyperclip.copy(alert_text)
    alert.accept()
    browser.get('https://stepik.org')
    time.sleep(10)
    cookies = pickle.load(open("cookies.pkl", "rb"))
    for cookie in cookies:
        browser.add_cookie(cookie)
    time.sleep(1)
    browser.refresh()
    browser.get('https://stepik.org/lesson/184253/step/6?unit=158843')
    time.sleep(5)
    browser.find_element_by_class_name('textarea').send_keys(pyperclip.paste())
    browser.find_element_by_class_name('submit-submission').click()
finally:
    time.sleep(5)
    browser.quit()