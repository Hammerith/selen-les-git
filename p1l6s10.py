from selenium import webdriver
import time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/registration2.html')
    elements = browser.find_elements_by_tag_name('input[required]')
    for element in elements:
        element.send_keys("yes")

    time.sleep(5)
    button = browser.find_element_by_css_selector('button.btn')
    button.click()
    time.sleep(2)
    welcome_text = browser.find_element_by_tag_name('h1')
    welcome = welcome_text.text
    assert "Congratulations! You have successfully registered!" == welcome

finally:
    time.sleep(7)
    browser.quit()
