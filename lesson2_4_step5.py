# Selenium Waits (Implicit Waits)
# используется вместо того, чтобы везде добавлять time.sleep()

# решение с использованием time.sleep() является плохим: оно не масштабируемое и трудно поддерживаемое

# в Selenium WebDriver есть специальный способ организации ожидания, который позволяет задать ожидание при
# инициализации драйвера, чтобы применить его ко всем тестам

# ожидание называется неявным (Implicit wait), так как его не надо явно указывать каждый раз,
# когда мы выполняем поиск элементов, оно автоматически будет применяться при вызове каждой последующей команды

from selenium import webdriver

browser = webdriver.Chrome()
# говорим WebDriver искать каждый элемент в течение 5 секунд
browser.implicitly_wait(5)

browser.get("http://suninjuly.github.io/wait1.html")

button = browser.find_element_by_id("verify")
button.click()
message = browser.find_element_by_id("verify_message")

assert "successful" in message.text

# теперь  на каждый вызов команды find_element WebDriver будет ждать 5 секунд до появления элемента на странице
# прежде, чем выбросить исключение NoSuchElementException


# Теперь мы знаем, как настроить ожидание поиска элемента. Во время поиска WebDriver каждые 0.5 секунды проверяет,
# появился ли нужный элемент в DOM-модели браузера (Document Object Model — «объектная модель документа»,
# интерфейс для доступа к HTML-содержимому сайта). Если произойдет ошибка,
# то WebDriver выбросит одно из следующих исключений (exceptions):

# Если элемент не был найден за отведенное время, то мы получим NoSuchElementException.

# Если элемент был найден в момент поиска, но при последующем обращении к элементу DOM (Document Object Model —
# «объектная модель документа», интерфейс для доступа к HTML-содержимому сайта) изменился,
# то получим StaleElementReferenceException. Например, мы нашли элемент Кнопка и через какое-то время
# решили выполнить с ним уже известный нам метод click. Если кнопка за это время была скрыта скриптом,
# то метод применять уже бесполезно — элемент "устарел" (stale) и мы увидим исключение.

# Если элемент был найден в момент поиска, но сам элемент невидим (например, имеет нулевые размеры),
# и реальный пользователь не смог бы с ним взаимодействовать, то получим ElementNotVisibleException.

# Знание причин появления исключений помогает отлаживать тесты и понимать, где находится баг в случае его возникновения.
