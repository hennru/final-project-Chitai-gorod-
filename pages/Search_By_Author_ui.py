from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.support import expected_conditions as EC


@allure.description("Поиск книги по автору на сайте Читай-город.")
class SearchByAuthor:
    def __init__(self, author_name: str):
        self.author_name = author_name

    def search_by_author(self, driver: webdriver.Chrome):
        with allure.step(f"Вводим имя автора '{self.author_name}' в поле поиска"):
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "search"))
            )
            search_input.clear()
            search_input.send_keys(self.author_name)

        with allure.step("Нажимаем кнопку поиска"):
            search_button = driver.find_element(
                By.CSS_SELECTOR, "button[aria-label='Найти']")
            search_button.click()

        with allure.step("Ожидаем появления результатов поиска"):
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".product-card__caption"))
            )

        with allure.step("Получаем автора первой книги в списке результатов"):
            author_element = driver.find_element(
                By.CSS_SELECTOR, "span.product-card__subtitle")
            author_text = author_element.text

        with allure.step(f"Найденный автор: '{author_text}'"):
            return author_text
