import requests
import random
from bs4 import BeautifulSoup

url = "https://taxi.yandex.ru/"
price_phrases = [
    "Сегодня минималочка:",
    "Цена вопроса:",
    "Готовь бабосы, стоимость —",
    "Копейка в копейку, выходит —",
    "Вот тебе ценничек:",
    "Не дешево, но нормально:",
    "А вот и цена:",
    "Тут уж как карта ляжет, но пока —",
    "Ну что, приготовился? Цена —",
    "Выходит по деньгам вот так:"
]

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}

response = requests.get(url, headers=headers)

def get_price():
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")

        # Поиск элементов с классом "priceText--oa4eD"
        price_elements = soup.find_all("span", class_="priceText--oa4eD")
        prices = [element.text.strip() for element in price_elements]

        if prices:
            return f"{random.choice(price_phrases)} {random.choice(prices)}"
        else:
            return "Цены не найдены, возможно, что-то изменилось на сайте."
    else:
        return f"Ошибка запроса: {response.status_code}"
