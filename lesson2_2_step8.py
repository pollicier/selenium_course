from selenium import webdriver
import os
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'

browser.get(link)

try:
    answer = 'text'
    first_name = browser.find_element_by_css_selector('body > div > form > div > input:nth-child(2)')
    first_name.send_keys(answer)
    last_name = browser.find_element_by_css_selector('body > div > form > div > input:nth-child(4)')
    last_name.send_keys(answer)
    email = browser.find_element_by_css_selector('body > div > form > div > input:nth-child(6)')
    email.send_keys(answer)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    print(current_dir)
    file_path = os.path.join(current_dir, 'file.txt')
    print(file_path)
    element = browser.find_element_by_css_selector('#file')
    element.send_keys(file_path)

    button = browser.find_element_by_css_selector('body > div > form > button')
    button.click()
    time.sleep(15)

finally:
    browser.quit()