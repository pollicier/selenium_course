from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'

browser.get(link)

try:
    n1 = browser.find_element_by_css_selector('#num1').text
    n2 = browser.find_element_by_css_selector('#num2').text
    s = int(n1) + int(n2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(s))
    accept_button = browser.find_element_by_css_selector('body > div > form > button')
    accept_button.click()
    time.sleep(15)

finally:
    browser.quit()