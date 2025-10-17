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
        # Ждём, пока строка поиска загрузится
        search_input = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search"))
        )
        search_input.clear()
        search_input.send_keys(self.author_name)

        # Клик по кнопке поиска
        search_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Найти']")
        search_button.click()

        # Ждём, пока появятся результаты
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".product-card__caption"))
        )

        # Получаем автора первой книги в списке
        author_element = driver.find_element(By.CSS_SELECTOR, "span.product-card__subtitle")
        return author_element.text