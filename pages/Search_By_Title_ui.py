import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.description("Класс для поиска книги по названию на сайте Читай-город.")
class SearchByTitle:
    def __init__(self, book_title: str):
        """Инициализация с названием книги для поиска"""
        self.book_title = book_title

    @allure.step("Ищем книгу по названию: '{self.book_title}'")
    def search_by_title(self, driver):
        with allure.step("Ожидаем появления поля поиска"):
            search_input = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.NAME, "search"))
            )
            search_input.clear()

        with allure.step(f"Вводим название книги: {self.book_title}"):
            search_input.send_keys(self.book_title)

        with allure.step("Нажимаем кнопку поиска"):
            search_button = driver.find_element(By.CSS_SELECTOR, "button[aria-label='Найти']")
            search_button.click()

        with allure.step("Ожидаем появления результатов поиска"):
            WebDriverWait(driver, 10).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, "a.product-card__title-link, .empty-search"))
            )

        with allure.step("Получаем название первой найденной книги"):
            book_element = driver.find_element(By.CSS_SELECTOR, ".product-card__title")
            return book_element.text
