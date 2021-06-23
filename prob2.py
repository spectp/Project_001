from selenium \
    import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()
browser.get(link)



time.sleep(1)

button_submit = browser.find_element_by_css_selector('.btn.btn-default')
button_submit.click()
# x_element = browser.find_elements_by_tag_name('option')
# for i in x_element:
#     x = int(i.get_attribute('value'))
#     if x == value_num:
#         x_element.click()
#         browser.find_element_by_css_selector('.btn.btn-default').click()
#         break
time.sleep(10)
browser.quit()






# x_element = browser.find_elements_by_tag_name('img')
# x = int(x_element.get_attribute('valuex'))
# y = calc(x)

# answer = browser.find_element_by_xpath('//input[@id="answer"]')
# answer.send_keys(str(y))
#
# checkbox = browser.find_element_by_xpath('//input[@id="robotCheckbox"]')
# checkbox.click()
#
# radiobutton = browser.find_element_by_xpath('//input[@value="robots"]')
# radiobutton.click()
#
# time.sleep(3)
#
# button_submit = browser.find_element_by_css_selector('.btn.btn-default')
# button_submit.click()

time.sleep(10)


