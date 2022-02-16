from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()

    alert = browser.switch_to.alert
    alert.accept()

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