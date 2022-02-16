from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "https://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.XPATH, "//span[@id='input_value']")
    x = x_element.text
    y = calc(x)

    text_field = browser.find_element(By.XPATH, "//input[@type='text']")
    text_field.send_keys(y)

    browser.execute_script("window.scrollBy(0, 100);")

    checkbox = browser.find_element(By.XPATH, "//input[@id='robotCheckbox']")
    checkbox.click()

    radiobutton = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    radiobutton.click()

    submit = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
