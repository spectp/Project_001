
from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    inputs = ['first', 'third', 'second']
    # Ваш код, который заполняет обязательные поля

    # inputs = ['first', 'third', 'second']
    # for i in inputs:
    #     part = browser.find_element_by_css_selector(".first_block .form-control." + i)
    #     insert = part.send_keys("Igor")
    input1 = browser.find_element_by_xpath('//input[contains(@placeholder, "first")]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath('//input[contains(@placeholder, "last")]')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath('//input[contains(@placeholder, "email")]')
    input3.send_keys("Smolensk")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()



'''учился прокурчивать страницу'''

# from selenium import webdriver
# import time
# import math
#
# def calc(x):
#   return str(math.log(abs(12 * math.sin(x))))
#
#
# link = "http://suninjuly.github.io/file_input.html"
#
# browser = webdriver.Chrome()
# browser.get(link)
#
# x_element = browser.find_element_by_xpath("//span[@id='input_value']")
# x = int(x_element.text)
# y = calc(x)
#
# answer = browser.find_element_by_xpath('//input[@id="answer"]')
# answer.send_keys(str(y))
#
# button = browser.find_element_by_tag_name("button")
#
# checkbox = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
# checkbox.click()
#
# browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#
# radiobutton = browser.find_element_by_xpath('//input[@value="robots"]')
# radiobutton.click()
#
# button.click()
#
# # успеваем скопировать код за 30 секунд
# time.sleep(30)
# # закрываем браузер после всех манипуляций
# browser.quit()
#
# # # не забываем оставить пустую строку в конце файла


'''Загружал файлы'''
# ﻿Если нам понадобится загрузить файл на веб-странице, мы можем использовать уже знакомый нам метод send_keys. Только теперь нам нужно в качестве аргумента передать путь к нужному файлу на диске вместо простого текста.
#
# Чтобы указать путь к файлу, можно использовать стандартный модуль Python для работы с операционной системой — os. В этом случае ваш код не будет зависеть от операционной системы, которую вы используете. Добавление файла будет работать и на Windows, и на Linux, и даже на MaсOS.
#
# Пример кода, который позволяет указать путь к файлу 'file.txt', находящемуся в той же папке, что и скрипт, который вы запускаете:
#
# import os
#
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# element.send_keys(file_path)
# Попробуйте добавить в файл отдельно команды print(os.path.abspath(__file__)) и print(os.path.abspath(os.path.dirname(__file__))) и посмотрите на разницу. Подробнее о методах модуля os можете почитать самостоятельно в документации: https://docs.python.org/3/library/os.path.html. Обратите внимание, что это будет работать только при запуске кода из файла, в интерпретаторе не сработает.
# Если совсем непонятно что происходит, пример:
#
# Допустим, мы написали код скрипта и сохранили код в lesson2_step7.py в свой локальной папке D:\stepik_homework. Активируем виртуальное окружение и запускаем его python lesson2_step7.py. В таком случае конструкция os.path.abspath(os.path.dirname(__file__)) вернет нам путь до директории файла с кодом, то есть D:\stepik_homework. В эту же папку кладем файл, который хотим прикрепить, то есть file.txt. Тогда, после выполнения команды:
#
# file_path = os.path.join(current_dir, 'file.txt')
#
# В переменной file_path будет полный путь к файлу 'D:\stepik_homework\file.txt'. Фишка в том, что если мы файлы lesson2_step7.py вместе с file.txt перенесем в другую папку, или на компьютер с другой ОС, то такой код без правок заработает и там.

'''Работал с алертами'''

# Теперь рассмотрим ситуацию, когда в сценарии теста возникает необходимость не только получить содержимое alert, но и нажать кнопку OK, чтобы закрыть alert. Alert является модальным окном: это означает, что пользователь не может взаимодействовать дальше с интерфейсом, пока не закроет alert. Для этого нужно сначала переключиться на окно с alert, а затем принять его с помощью команды accept():
#
# alert = browser.switch_to.alert
# alert.accept()
# Чтобы получить текст из alert, используйте свойство text объекта alert:
#
# alert = browser.switch_to.alert
# alert_text = alert.text
# Другой вариант модального окна, который предлагает пользователю выбор согласиться с сообщением или отказаться от него, называется confirm. Для переключения на окно confirm используется та же команда, что и в случае с alert:
#
# confirm = browser.switch_to.alert
# confirm.accept()
#
#
# Для confirm-окон можно использовать следующий метод для отказа:
#
# confirm.dismiss()
# То же самое, что и при нажатии пользователем кнопки "Отмена".
#
# Третий вариант модального окна — prompt — имеет дополнительное поле для ввода текста. Чтобы ввести текст, используйте метод send_keys():
#
# prompt = browser.switch_to.alert
# prompt.send_keys("My answer")
# prompt.accept()


'''Переходил по вкладкам'''

# При работе с веб-приложениями приходится переходить по ссылкам, которые открываются в новой вкладке браузера. WebDriver может работать только с одной вкладкой браузера. При открытии новой вкладки WebDriver продолжит работать со старой вкладкой. Для переключения на новую вкладку надо явно указать, на какую вкладку мы хотим перейти. Это делается с помощью команды switch_to.window:
#
# browser.switch_to.window(window_name)
# Чтобы узнать имя новой вкладки, нужно использовать метод window_handles, который возвращает массив имён всех вкладок. Зная, что в браузере теперь открыто две вкладки, выбираем вторую вкладку:
#
# new_window = browser.window_handles[1]
# Также мы можем запомнить имя текущей вкладки, чтобы иметь возможность потом к ней вернуться:
#
# first_window = browser.window_handles[0]

'''ожидание для поиска'''

#
# Идеальное решение могло бы быть таким: нам всё равно надо избежать ложного падения тестов из-за асинхронной работы скриптов или задержек от сервера, поэтому мы будем ждать появление элемента на странице в течение заданного количества времени (например, 5 секунд). Проверять наличие элемента будем каждые 500 мс. Как только элемент будет найден, мы сразу перейдем к следующему шагу в тесте. Таким образом, мы сможем получить нужный элемент в идеальном случае сразу, в худшем случае за 5 секунд.
#
# В Selenium WebDriver есть специальный способ организации такого ожидания, который позволяет задать ожидание при инициализации драйвера, чтобы применить его ко всем тестам. Ожидание называется неявным (Implicit wait), так как его не надо явно указывать каждый раз, когда мы выполняем поиск элементов, оно автоматически будет применяться при вызове каждой последующей команды.
#
# Улучшим наш тест с помощью неявных ожиданий. Для этого нам нужно будет убрать time.sleep() и добавить одну строчку с методом implicitly wait:
#
# from selenium import webdriver
#
# browser = webdriver.Chrome()
# # говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)
#
# browser.get("http://suninjuly.github.io/wait1.html")
#
# button = browser.find_element_by_id("verify")
# button.click()
# message = browser.find_element_by_id("verify_message")
#
# assert "successful" in message.text
# Теперь мы можем быть уверены, что при небольших задержках в работе сайта наши тесты продолжат работать стабильно. На каждый вызов команды find_element WebDriver будет ждать 5 секунд до появления элемента на странице прежде, чем выбросить исключение NoSuchElementException.