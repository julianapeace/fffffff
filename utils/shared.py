import requests
import datetime
import pytz

def generate_timestring(wen_buy, wen_sell):
    #  "2021-04-16T22:19:19.8000000Z"
    dt_buy = str(datetime.date.fromisoformat(wen_buy)).split(" ")[0] + "T22:19:19.8000000Z"

    if wen_sell == 'today':
        dt_sell = str(datetime.datetime.now()).split(" ")[0] + "T22:19:19.8000000Z"
    else:
        dt_sell = wen_sell + "T22:19:19.8000000Z"

    return [dt_buy, dt_sell]


def get_rates(urls, api_key):
    headers = {'X-CoinAPI-Key' : api_key}
    results = []
    for i in urls:
        response = requests.get(i, headers=headers)
        json = response.json()
        print(json)
        results.append(json['rate'])
    return results

def generate_urls(token, wen_buy, wen_sell='today'):
    urls = []

    asset_id_base = token.upper()
    asset_id_quote = 'USD'

    wens = generate_timestring(wen_buy, wen_sell)

    wen_buy = wens[0]
    wen_buy_url = 'https://rest.coinapi.io/v1/exchangerate/' + asset_id_base + '/' + asset_id_quote + '?time=' + wen_buy
    urls.append(wen_buy_url)

    if wen_sell != 'today':
        wen_sell = wens[1]
        wen_sell_url = 'https://rest.coinapi.io/v1/exchangerate/' + asset_id_base + '/' + asset_id_quote + '?time=' + wen_sell
        urls.append(wen_sell_url)
    else:
        wen_sell_url = 'https://rest.coinapi.io/v1/exchangerate/' + asset_id_base + '/' + asset_id_quote
        urls.append(wen_sell_url)
    return urls
