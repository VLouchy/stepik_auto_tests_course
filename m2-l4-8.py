from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

# говорим Selenium проверять в течение 12 секунд

WebDriverWait(browser, 30).until(EC.text_to_be_present_in_element((By.ID, "price"), '$100'))

browser.find_element(By.ID, "book").click()

x_value = browser.find_element(By.ID, "input_value").text
y = calc(x_value)

input1 = browser.find_element(By.ID, "answer")
input1.send_keys(y)

button = browser.find_element(By.ID, "solve")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
button.click()

time.sleep(10)

