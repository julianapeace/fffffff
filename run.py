import click
import os
import requests
from os.path import join, dirname
from dotenv import load_dotenv
from utils.shared import generate_urls, get_rates
from utils.ascii_art import *

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

coinapi_api_key = os.environ.get("coinapi_api_key")

# when buy? 04/21/2021 50 btc
# when sell? 09/14/2021
# You would've made $1,000,000
# insert asci fffffffffff meme

@click.command()
@click.option('--token', prompt='token', help='token')
@click.option('--wen_buy', prompt='wen buy (example: 2019-12-04)', help='wen')
@click.option('--wen_sell', default='today', prompt='wen sell (example: 2019-12-04)')
@click.option('--how_much_money', prompt='how much cash', help='how much much could you have spent on crypto that day?')


def cli(token, wen_buy, wen_sell, how_much_money):
    """ fffffigure how much you fffffucked up """

    urls = generate_urls(token, wen_buy, wen_sell)

    rates = get_rates(urls, coinapi_api_key)

    num_of_tokens = int(how_much_money) / int(rates[0])
    
    for i in range(8):
        print(".")

    print('you could have bought ', num_of_tokens, " ", token.upper(), " with the $", how_much_money, "on ", wen_buy)

    net = (num_of_tokens*rates[1]) - int(how_much_money)

    if (net > 0):
        print('You could have made ', net, "if you sold", wen_sell)
        return rage()
    else:
        print('You could have lost ', net,  "if you sold", wen_sell)
        return better_than_expected()


if __name__ == '__main__':
    cli()
    # cli('btc', '2019-12-04', 'today', 9000) # in testing
