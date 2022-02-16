from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    price = WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.XPATH, "//h5[@id='price']"), "100"))
    button = browser.find_element(By.XPATH, "//button[@id='book']")
    button.click()

    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    input_field = browser.find_element(By.XPATH, "//input[@name='text']")
    input_field.send_keys(y)

    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()