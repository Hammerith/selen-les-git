from selenium import webdriver
import os, time

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')
    # открываем ссылку
    for selector in ['[name = "firstname"]', '[name = "lastname"]', '[name = "email"]']:
        browser.find_element_by_css_selector(selector).send_keys('ha')
    # находим поля для заполнения и заполняем их
    current_dir = os.path.abspath(os.path.dirname(__file__))
    # находим путь к папке с данным файлом
    file_path = os.path.join(current_dir, 'file.txt')
    # составляем путь файла из пути директории + название файла
    element = browser.find_element_by_css_selector('[type="file"]').send_keys(file_path)
    # находим кнопку "выберите файл" и загружаем в нее наш файл посредством передачи пути
    browser.find_element_by_css_selector('.btn').click()
    # находим и кликаем submit

finally:
    time.sleep(5)
    browser.quit()

