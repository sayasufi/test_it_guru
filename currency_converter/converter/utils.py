import requests
import xml.etree.ElementTree as ET
from decimal import Decimal


def fetch_exchange_rates() -> dict:
    """
    Получает текущие курсы валют с XML-канала Центрального банка России и список доступных валют.

    Эта функция получает данные о курсах валют с указанного URL, парсит XML-ответ и извлекает курсы валют.
    Также включен российский рубль (RUB) с фиксированным курсом 1.0.

    Возвращает:
        dict: Словарь с двумя ключами:
            - 'rates': Словарь, где ключи - коды валют (например, 'USD', 'EUR'), а значения - курсы валют относительно RUB.
            - 'currencies': Список доступных валют (например, ['USD', 'EUR']).
    """
    url = "https://www.cbr-xml-daily.ru/daily.xml"
    response = requests.get(url)
    response.raise_for_status()

    tree = ET.ElementTree(ET.fromstring(response.content))
    root = tree.getroot()

    rates = {'RUB': Decimal('1.0')}  # Добавление российского рубля с фиксированным курсом
    currencies = ['RUB']
    for currency in root.findall('Valute'):
        char_code = currency.find('CharCode').text
        value = currency.find('Value').text
        nominal = int(currency.find('Nominal').text)
        rate = Decimal(value.replace(',', '.')) / Decimal(nominal)
        rates[char_code] = rate
        currencies.append(char_code)

    return {'rates': rates, 'currencies': currencies}
