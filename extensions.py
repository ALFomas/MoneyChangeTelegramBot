import requests
import json
from config import *


class ConvertionException(Exception):
    """:exception class"""
    pass


class ManyConverter:
    """currency exchange class"""

    @staticmethod
    def get_price(quote: str, base: str, amount: str) -> float:
        """currency exchange method using min-api.cryptocompare.com"""

        if quote == base:
            raise ConvertionException(f'Перевод {base} к {quote} один к одному.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'{quote} не в списке доступных валют \n /values для отображения доступных валют')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'{base} не в списке доступных валют \n /values для отображения доступных валют')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'{amount} неадекватное значение для суммы')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        price = json.loads(r.content)[keys[base]]
        total_price = float(price) * float(amount)
        return total_price
