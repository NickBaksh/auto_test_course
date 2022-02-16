from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

try:
    link = "https://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_element = browser.find_element(By.XPATH, "//span[@id='num1']")
    x = x_element.text

    y_element = browser.find_element(By.XPATH, "//span[@id='num2']")
    y = y_element.text
    sum = int(x) + int(y)
    sum = str(sum)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(sum)

    submit = browser.find_element(By.CSS_SELECTOR, ".btn")
    submit.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
