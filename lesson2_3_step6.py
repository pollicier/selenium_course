from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'

browser.get(link)

try:
    window_before = browser.window_handles[0]

    magic_button = browser.find_element_by_css_selector('body > form > div > div > button')
    magic_button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    value = browser.find_element_by_css_selector('#input_value').text
    print(value)
    y = str(math.log(abs(12*math.sin(int(value)))))
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)

    accept_button = browser.find_element_by_css_selector('body > form > div > div > button')
    accept_button.click()

    time.sleep(15)

finally:
    browser.quit()