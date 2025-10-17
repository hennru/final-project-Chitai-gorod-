from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure

@allure.description("Тестирование добавления товара в корзину на сайте Читай-город.")
class AddToCart:

    def __init__(self, book_title: str):
        """Создает объект для добавления книги в корзину."""
        self.book_title = book_title

    def search_by_title(self, driver: webdriver.Chrome) -> None:
        """Ищет книгу по названию и добавляет её в корзину."""

        wait = WebDriverWait(driver, 10)  # Настройка ожидания

        # Ввод названия книги в строку поиска
        search_input = wait.until(EC.presence_of_element_located((By.NAME, "search")))
        search_input.clear()
        search_input.send_keys(self.book_title)
        search_input.send_keys(Keys.RETURN)  # Нажимаем Enter вместо кнопки поиска

          # Найти все кнопки "Купить" на странице
        buy_buttons = driver.find_elements(By.CSS_SELECTOR, ".product-buttons__main-action .chg-app-button__content")
        for btn in buy_buttons:
            if btn.text.strip() == "Купить":
                btn.click()
                break

        # Открытие корзины
        cart_icon = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.header-cart__icon')))
        cart_icon.click()