import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    browser = webdriver.Chrome()


    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID,"price"),"$100"))
    browser.find_element(By.ID,"book").click()
    x = int(browser.find_element(By.ID, "input_value").text)
    Keys.END
    browser.find_element(By.ID, "answer").send_keys(math.log(math.fabs(12*math.sin(x))))
    browser.find_element(By.ID, "solve").click()



# Пиши код выше ^

finally:
# НЕ УДАЛЯТЬ!!!!!
    time.sleep(5)
    browser.quit()