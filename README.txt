final-project-Chitai-gorod-
Ссылка на финальный проект по ручному тестированию---https://skyprodzz.yonote.ru/share/3e007677-2dd4-4d50-abd4-0753c801b7ae
Автоматизация тестирования сайта "Читай-город"

Проект предназначен для автоматизации UI и API-тестов сайта [Читай-город](https://www.chitai-gorod.ru) с использованием Selenium и Python. Тесты проверяют функциональность поиска, добавления и удаления книг из корзины, а также проверяют API-запросы.
---
🛠 Используемые технологии
- Python 3.13+
- Selenium WebDriver
- pytest
- requests (для API-тестов)
- Allure для генерации отчетов
- Google Chrome + chromedriver

 📂 Структура проекта
Chitai-gorod/
│
├── pages/ # Page Objects (модели страниц)
│ ├── Search_by_author_ui.py
│ ├── Search_by_title_ui.py
│ ├── Add_to_cart_ui.py
│ └── Delete_from_cart_ui.py
| └── Add_To_Cart_api.py
| └── Delete_From_Cart_api.py
| └── Send_Empty_Post_Request_api.py
| └── Update_cart_api.py
│ └── Wrong_Add_To_Cart_api.py
├── test/ # Тесты
│ ├── test_ui.py
│ └── test_api.py 
├── constants.py
├── requirements.txt # Зависимости проекта
├── README.md # Документация проекта
└── .gitignore

⚙ Установка
 Клонируйте репозиторий:  
```bash
git clone <URL_репозитория>
cd Chitai-gorod
```
Создайте виртуальное окружение (рекомендуется):
python -m venv venv
source venv/bin/activate      # Linux/Mac
venv\Scripts\activate         # Windows

Установите зависимости: pip install -r requirements.txt

Убедитесь, что chromedriver установлен и доступен в PATH:
Скачать ChromeDriver
Версия chromedriver должна совпадать с версией браузера Google Chrome.

🚀 Запуск тестов
Запуск всех UI тестов: 
pytest -k test_ui.py
Запуск конкретного теста: 
pytest -k test_add_to_cart
Запуск тестов с генерацией отчета Allure (Windows PowerShell):
pytest test/test_ui.py --alluredir=allure-results
allure serve allure-results
Для Linux/Mac:
pytest test/test_ui.py --alluredir=allure-results && allure serve allure-results

API-тесты
Пример запуска всех API-тестов:
pytest -k test_api.py
Запуск с Allure отчетом:
pytest test/test_api.py --alluredir=allure-results
allure serve allure-results

📄 Формат отчетов Allure
После выполнения тестов можно открыть интерактивный отчет Allure командой:
allure serve allure-results

Отчет покажет:
Статус тестов (пройден/провален)
Скриншоты ошибок (для UI тестов)
Степы выполнения тестов (если использовался allure.step)
Подробные логирования

🔧 Настройка тестов
Для корректной работы UI-тестов нужно обновлять селекторы в случае изменения структуры сайта.
В API-тестах используется библиотека requests для HTTP-запросов.
В тестах используются WebDriverWait и ExpectedConditions для стабильной работы.
Для кооректной работы API-тестов понадобиться токен и id товара. Все это можно получить при нахождении на сайте
Читай-города с помощью инструментов разработчика (F12 вкладка Network)
 📌 Рекомендации
Проверять актуальность селекторов перед запуском UI-тестов.
Использовать виртуальное окружение для управления зависимостями.
Сохранять Chrome и chromedriver одной версии.
Включать Allure степы и описание тестов для удобного анализа результатов.
Для API-тестов проверять актуальные эндпоинты и структуру ответа.
