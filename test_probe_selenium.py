from selenium import webdriver
import time
import math
import  os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# def calc(x):
#   return str(math.log(abs(12 * math.sin(x))))
#
#
# link = "http://suninjuly.github.io/explicit_wait2.html"
#
# browser = webdriver.Chrome()
# browser.get(link)

# button = browser.find_element_by_xpath("//button[@type='submit']")
# price = WebDriverWait(browser, 12).until(
#         EC.text_to_be_present_in_element((By.ID, "price"), '$100')
#     )
# button = browser.find_element_by_id("book")
# button.click()

# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)

# time.sleep(1)
# x_element = browser.find_element_by_xpath("//span[@id='input_value']")
# x = int(x_element.text)
# y = calc(x)
#
# answer = browser.find_element_by_xpath('//input[@id="answer"]')
# answer.send_keys(str(y))
# #
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
# first = browser.find_element_by_name('firstname')
# first.send_keys('Иван')
# last = browser.find_element_by_name('lastname')
# last.send_keys('Petrov')
# email = browser.find_element_by_name('email')
# email.send_keys('111@bk.ru')
#
# file = browser.find_element_by_xpath("//input[@type='file']")
# current_dir = os.path.abspath(os.path.dirname('D:\seleniumfile.txt'))
# file_path = os.path.join(current_dir, 'seleniumfile.txt')
# file.send_keys(file_path)



#
# button = browser.find_element_by_xpath("//button[@type='submit']")
# button.click()


# успеваем скопировать код за 30 секунд
# time.sleep(10)
# закрываем браузер после всех манипуляций
# browser.quit()

# # не забываем оставить пустую строку в конце файла



import unittest

class TestAbs(unittest.TestCase):
    from selenium import webdriver

    def test1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath('//input[@placeholder="Input your first name"]')
        input1.send_keys('Ваня')
        input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
        input2.send_keys('Иванов')
        input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
        input3.send_keys('dwa@bk.ru')
        input4 = browser.find_element_by_xpath('//input[@placeholder="Input your phone:"]')
        input4.send_keys('79996665544')
        input5 = browser.find_element_by_xpath('//input[@placeholder="Input your address:"]')
        input5.send_keys('Москва')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        browser.quit()





    def test2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        input1 = browser.find_element_by_xpath('//input[@placeholder="Input your name"]')
        input1.send_keys('Ваня')
        input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
        input2.send_keys('Иванов')
        input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
        input3.send_keys('dwa@bk.ru')
        input4 = browser.find_element_by_xpath('//input[@placeholder="Input your phone"]')
        input4.send_keys('79996665544')
        input5 = browser.find_element_by_xpath('//input[@placeholder="Input your address"]')
        input5.send_keys('Москва')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()
        browser.quit()





