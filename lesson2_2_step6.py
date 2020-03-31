from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
link = 'http://SunInJuly.github.io/execute_script.html'

browser.get(link)

try:
    value = browser.find_element_by_css_selector('#input_value').text
    y = str(math.log(abs(12*math.sin(int(value)))))
    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)

    checkbox = browser.find_element_by_css_selector('#robotCheckbox')
    browser.execute_script("return arguments[0].scrollIntoView(true);", checkbox)
    checkbox.click()
    radio = browser.find_element_by_css_selector('#robotsRule')
    radio.click()
    button = browser.find_element_by_css_selector('body > div > form > button')
    button.click()
    time.sleep(15)

finally:
    browser.quit()