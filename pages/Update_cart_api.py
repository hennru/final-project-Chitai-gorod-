import requests
import json
import allure
from constants import API1_url, API2_url, bearer_token


@allure.description("Тестирование добавления товара в корзину на сайте Читай-город.")
class UpdateCartAPI:

    # URL для работы с корзиной (например, для получения информации о корзине)
    url = API1_url
    url_2 = API2_url  # URL для обновления корзины

    def __init__(self, url):
        """
                  Инициализация класса UpdateCartAPI.

                 :param url: URL, используемый для работы с корзиной.
        """
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',  # Установка типа содержимого для JSON
            'Authorization': bearer_token  # Авторизационный токен для доступа к API
        }

    @allure.step("Обновление содержимого корзины")
    def update_cart(self, items: dict) -> tuple:

        # Отправляем PUT-запрос для редактирования корзины
        response = requests.put(
            self.url_2, headers=self.headers, data=json.dumps(items))
        # Возвращаем статус-код и текст ответа от сервера
        return response.status_code, response.text
