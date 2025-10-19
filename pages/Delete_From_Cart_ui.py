import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@allure.description("Класс для удаления книги из корзины на сайте Читай-город.")
class DeleteFromCart:
    def __init__(self, book_title: str):
        """Инициализация с названием книги для удаления"""
        self.book_title = book_title

    @allure.step("Удаляем книгу '{self.book_title}' из корзины")
    def delete_book_from_cart(self, driver):
        with allure.step("Открываем корзину"):
            cart_button = driver.find_element(
                By.CSS_SELECTOR, "a.header-cart-link")
            cart_button.click()

        with allure.step(f"Ищем книгу в корзине: {self.book_title}"):
            book_in_cart = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, f"//a[contains(text(), '{self.book_title}')]"))
            )

        with allure.step("Нажимаем кнопку удаления книги"):
            delete_button = book_in_cart.find_element(
                By.XPATH, "../..//button[contains(@class,'cart-item__remove')]")
            delete_button.click()

        with allure.step("Ожидаем удаления книги из корзины"):
            WebDriverWait(driver, 10).until(EC.staleness_of(book_in_cart))
