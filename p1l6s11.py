from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/registration2.html')
    element = browser.find_element_by_css_selector(".first_block .form-control.first")
    element.send_keys("yes")
    element = browser.find_element_by_css_selector(".first_block .form-control.second")
    element.send_keys("yes")
    element = browser.find_element_by_css_selector(".first_block .form-control.third")
    element.send_keys("yes")

    time.sleep(2)
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    time.sleep(2)
    welcome_text = browser.find_element_by_tag_name('h1')
    welcome = welcome_text.text
    assert "Congratulations! You have successfully registered!" == welcome

finally:
    time.sleep(5)
    browser.quit()
