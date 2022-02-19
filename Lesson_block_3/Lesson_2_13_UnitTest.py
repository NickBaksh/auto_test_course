from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestUniqueSelector (unittest.TestCase):
    def test_UniqueSelector1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        First_name = browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input")
        First_name.send_keys('Nikita')
        Last_name = browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input")
        Last_name.send_keys('Baksh')
        Email = browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input")
        Email.send_keys('nikita@django.com')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Welcome text is not equal")

    def test_UniqueSelector2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        First_name = browser.find_element(By.XPATH, "//label[text()='First name*']/following-sibling::input")
        First_name.send_keys('Nikita')
        Last_name = browser.find_element(By.XPATH, "//label[text()='Last name*']/following-sibling::input")
        Last_name.send_keys('Baksh')
        Email = browser.find_element(By.XPATH, "//label[text()='Email*']/following-sibling::input")
        Email.send_keys('nikita@django.com')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text,
                         "Welcome text is not equal")


if __name__ == "__main__":
    unittest.main()