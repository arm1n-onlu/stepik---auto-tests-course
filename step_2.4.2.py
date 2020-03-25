from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import  math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    price = WebDriverWait(browser, 13).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"$100")
)
    button = browser.find_element_by_id('book')
    button.click()
    num1 = browser.find_element_by_id('input_value')
    x = num1.text
    y = calc(x)
    answ = browser.find_element_by_id('answer')
    answ.send_keys(y)
    button1 = browser.find_element_by_id('solve')
    button1.click()
finally:
    time.sleep(5)
    browser.quit()