from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/math.html'
browser.get(link)


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    x_element = browser.find_element_by_css_selector('#input_value')
    x = x_element.text
    y = calc(x)

    textarea = browser.find_element_by_css_selector('#answer')
    textarea.send_keys(y)

    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()

    radio = browser.find_element_by_css_selector('#robotsRule')
    radio.click()

    accept_button = browser.find_element_by_css_selector('body > div > form > button')
    accept_button.click()

    time.sleep(10)

finally:
    browser.quit()