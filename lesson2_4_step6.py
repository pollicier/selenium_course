# ЗАДАНИЕ ДЛЯ ОПРЕДЕЛЕНИЯ ОШИБКИ

from selenium import webdriver

browser = webdriver.Chrome()
browser.implicitly_wait(5)

link = 'http://suninjuly.github.io/cats.html'
browser.get(link)

try:
    button = browser.find_element_by_id("button")
finally:
    browser.quit()