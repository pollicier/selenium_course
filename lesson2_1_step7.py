from selenium import webdriver
import math
import time

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()

browser.get(link)

try:
    gold_chest = browser.find_element_by_css_selector('#treasure')
    value = gold_chest.get_attribute("valuex")

    y = str(math.log(abs(12*math.sin(int(value)))))

    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)

    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    checkbox.click()

    radio = browser.find_element_by_css_selector('#robotsRule')
    radio.click()

    accept_button = browser.find_element_by_css_selector('body form button')
    accept_button.click()

    time.sleep(15)

finally:
    browser.quit()