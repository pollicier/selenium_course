# Explicit Waits (WebDriverWait и expected_conditions)

# чтобы тест был надежным, нам нужно не только найти кнопку на странице,
# но и дождаться, когда кнопка станет кликабельной.
# для реализации подобных ожиданий существует понятие ЯВНЫХ ожиданий (Explicit Waits),
# которые позволяют задать специальное ожидание для конкретного элемента

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/wait2.html")

# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
button = WebDriverWait(browser, 5).until(
        ec.element_to_be_clickable((By.ID, "verify"))
    )
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

# element_to_be_clickable вернет элемент, когда он станет кликабельным, или вернет False в ином случае

# в модуле expected_conditions есть много другиъ правил, которые позволяют реализовывать необходимые ожидания
# ПОДРОБНЕЕ https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.support.expected_conditions

# если мы захотим проверять, что кнопка становится неактивной после отправки данных, то можно задать
# негативное правило с помощью метода until_not:

# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной
button = WebDriverWait(browser, 5).until_not(
        EC.element_to_be_clickable((By.ID, "verify"))
    )
