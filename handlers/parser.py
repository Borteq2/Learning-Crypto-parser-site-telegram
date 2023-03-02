import time
import requests

from bs4 import BeautifulSoup
from handlers.telegram import send_notify
from handlers.menu import TaskHandler


def get_crypto_rank(coins):
    result = {}
    html_resp = requests.get("https://coinranking.com/ru").text
    block = BeautifulSoup(html_resp, "lxml")
    rows = block.find_all("tr", class_="table__row--full-width")

    for row in rows:
        ticker = row.find("span", class_="profile__subtitle-name")
        if ticker:
            ticker = ticker.text.strip().lower()

            if ticker in coins:
                price = row.find("td", class_="table__cell--responsive")
                if price:
                    price = int(float(price.find("div", class_="valuta--light").text\
                                .replace("$", "").replace(",", ".").replace(" ", "")\
                                .replace("\n", "").replace("\xa0", "")))
                result[ticker.lower()] = price
    return result


def check_coins_balance():
    while True:
        coins = TaskHandler.read_task_file()
        coin_dict = get_crypto_rank(coins.keys())

        for name, price in coins.items():
            if name in coin_dict:
                if coin_dict[name] <= int(price):
                    send_notify(f'[{name}] - buy\nprice: {coin_dict[name]}')
                    TaskHandler.delete_tasks_in_file(name, update=False)

        time.sleep(10)

