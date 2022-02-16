from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os


try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    name = browser.find_element(By.XPATH, "//input[@name='firstname']")
    name.send_keys("Имя")

    last_name = browser.find_element(By.XPATH, "//input[@name='lastname']")
    last_name.send_keys("Фамилия")

    mail = browser.find_element(By.XPATH, "//input[@name='email']")
    mail.send_keys("kkk@gmail.com")

    file_button = browser.find_element(By.XPATH, "//input[@id='file']")

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    file_button.send_keys(file_path)

    submit_button = browser.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
