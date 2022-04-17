import os
import json
import requests
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
coinapi_api_key = os.environ.get("coinapi_api_key")

# url = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
asset_id_base = 'BTC'
asset_id_quote = 'USD'
time = '2021-04-16T22:19:19.8000000Z'
url = 'https://rest.coinapi.io/v1/exchangerate/' + asset_id_base + '/' + asset_id_quote + '?time=' + time
# https://rest.coinapi.io/v1/exchangerate/BTC/USD?time=2021-04-16T22:19:19.8000000Z
headers = {'X-CoinAPI-Key' : coinapi_api_key}
response = requests.get(url, headers=headers)

print(response)

# The above command returns JSON structured like this:
#
# {
#   "time": "2017-08-09T14:31:18.3150000Z",
#   "asset_id_base": "BTC",
#   "asset_id_quote": "USD",
#   "rate": 3260.3514321215056208129867667
# }
