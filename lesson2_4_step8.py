from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import math
import time

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/explicit_wait2.html'

browser.get(link)
browser.implicitly_wait(15)

try:
    book_button = WebDriverWait(browser, 15).until(
        ec.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'), '$100')
    )
    book_button_click = browser.find_element_by_css_selector('#book').click()

    wait = WebDriverWait(browser, 5)
    value_search = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, '#input_value')))

    value = browser.find_element_by_css_selector('#input_value').text
    print(value)
    y = str(math.log(abs(12 * math.sin(int(value)))))

    answer = browser.find_element_by_css_selector('#answer')
    answer.send_keys(y)

    sub_button = browser.find_element_by_css_selector('#solve')
    sub_button.click()

    time.sleep(15)

finally:
    browser.quit()