import requests
from dataclasses import dataclass
from typing import Final

BASE_URL: Final[str] = 'https://api.coingecko.com/api/v3/coins/markets'


@dataclass
class Coin:
    name: str
    symbol: str
    current_price: float
    highest_24h: float
    lowest_24h: float
    price_change_24h: float
    price_change_percentage_24h: float

    def __str__(self):
        return f'{self.name}({self.symbol}): ${self.current_price}'


def get_coins() -> list[Coin]:
    payload: dict = {'vs_currency': 'USD', 'order': 'market_cap_desc'}
    data = requests.get(BASE_URL, params=payload)
    json: dict = data.json()

    coin_list: list[Coin] = []
    for item in json:
        current_coin: Coin = Coin(name=item.get('name'),
                                  symbol=item.get('symbol'),
                                  current_price=item.get('current_price'),
                                  highest_24h=item.get('highest_24h'),
                                  lowest_24h=item.get('lowest_24h'),
                                  price_change_24h=item.get('price_change_24h'),
                                  price_change_percentage_24h=item.get('price_change_percentage_24h'))
        coin_list.append(current_coin)

    return coin_list


def alert(symbol: str, bottom: float, top: float, coins_list: list[Coin]):
    for coin in coins_list:
        if coin.symbol == symbol:
            if coin.current_price > top or coin.current_price < bottom:
                print(coin, 'TRIGGERED!!!')
            else:
                print(coin)


if __name__ == '__main__':
    coins: list[Coin] = get_coins()

    alert('btc', bottom=20_000, top=28_000, coins_list=coins)
    alert('eth', bottom=1800, top=1900, coins_list=coins)
    alert('xpr', bottom=0.47, top=0.48, coins_list=coins)
