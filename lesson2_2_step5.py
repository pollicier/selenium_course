# метод execute_script
# execute_script(javascript_code)

# пример 1
from selenium import webdriver
browser = webdriver.Chrome()
browser.execute_script("alert('Robots at work');")

# можно выполнять сразу несколько инструкций, перчислив их через точку с запятой
browser.execute_script("document.title='Script executing';alert('Robots at work');")

# пример 2 (если один элемент оказался перекрыт другим, например, футером)
# используется скрипт "return arguments[0].scrollIntoView(true);"
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

# подробнее о методе https://developer.mozilla.org/ru/docs/Web/API/Element/scrollIntoView

# можно проскролить страницу на заданное число пикселей
browser.execute_script("window.scrollBy(0, 100);")

