# import requests
import apiKey
import pandas as pd
from time import sleep
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
    'start': '1',
    'limit': '5000',
    'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': apiKey.COINMARKETCAP_API_KEY,
}

session = Session()
session.headers.update(headers)

df = pd.DataFrame(columns=[
    'symbol',
    'name',
    'price',
    'volume_24',
    'perc_change_1h',
    'perc_change_24h',
    # 'market_cap'
])


def get_data(df):
    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        all_currency_list = data['data']
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)

    for currency in all_currency_list:
        raw_data = {
            'symbol': currency["symbol"],
            'name': currency["name"],
            'price': currency["quote"]["USD"]["price"],
            'volume_24h': currency["quote"]["USD"]["volume_24h"],
            'perc_change_1h': currency["quote"]["USD"]["percent_change_1h"],
            'perc_change_24h': currency["quote"]["USD"]["percent_change_24h"],
            # 'market_cap': currency["quote"]["USD"]["market_cap"]
        }

        df = df.append(raw_data, ignore_index=True)

    return df


# df.to_csv('crypto_data.csv')
currencies = [
    'BTC',
    'ETH',
    'BNB',
    'DOT',
    'LTC',
    'MATIC',
    'VET',
    'FIL',
    'EOS',
    'TRX',
    'BTT',
    'DASH',
    'ENJ',
    'HBAR',
    'DOGE'
]


def abrupt_change_alert(df, currencies):
    for currency in currencies:
        change = float(df[df['symbol'] == currency]['perc_change_1h'].item())
        if change > 5:
            details = f'{currency}: {change}, Value Incresing Really Fast!!! Invest Now!!!'
        elif change > 3:
            details = f'{currency}: {change}, Value Incresing Fast!!! Check News, and invest if reliable.'
        elif change < -3:
            details = f'{currency}: {change}, Value Decreasing Fast!!! Check News, and sell or leave depending on the situation.'
        elif change < -5:
            details = f'{currency}: {change}, Value Decreasing Really Fast!!! Sell Now!!!'
        # else:
        #     print('No unusual activity.')


while True:
    print('-' * 50)

    try:
        df = get_data(df)
        abrupt_change_alert(df, currencies)
    except Exception as e:
        print('Couldn\'t retrieve the data!...Try again')

    # Run every 15 minutes
    sleep(90)
