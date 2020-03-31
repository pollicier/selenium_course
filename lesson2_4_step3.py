# как работают методы get и find_element

from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

# если выполнить тест вручную - тест завершится успешно, в случае автотеста - он упадет с сообщением
# NoSuchElementException для элемента с id = "verify"
# это происходит из-за того, что команды в Python выполняются синхронно (последовательно)

# когда мы знаем, что кнопка появляется с задержкой, мы можем добавить пауку до начала поиска элемента

from selenium import webdriver
import time

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/wait1.html")

time.sleep(1)
button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text
