# Lessun10 成り行き買い
# ライブラリのインポート
import configparser
import hmac
import hashlib
import json
from pprint import pprint
import time

import requests

conf = configparser.ConfigParser()
conf.read("config.ini")

ACCESS_KEY = conf["coincheck"]["access_key"]
SERCRET_KEY = conf["coincheck"]["sercret_key"]

# URLの設定
BASE_URL = "https://coincheck.com"
url = BASE_URL + "/api/exchange/orders"

nonce = str(int(time.time()))

params = {
    "pair": "btc_jpy",
    "order_type" : "market_buy",
    "market_buy_amount" : 16000
}

body = json.dumps(params)
message = nonce + url + body

signature = hmac.new(SERCRET_KEY.encode(),
                     message.encode(),
                     hashlib.sha256).hexdigest()

headers = {
    "ACCESS-KEY": ACCESS_KEY,
    "ACCESS-NONCE": nonce,
    "ACCESS-SIGNATURE": signature,
    "Content-Type": "application/json"
}


# r = requests.get(url, params=params)
#r = requests.get(url, headers=headers)
r = requests.post(url, headers=headers,data=body)
r = r.json()
# pprint(r["asks"][::-1])
# pprint(r["bids"])
pprint(r)


# 実行結果
# 　　{'amount': None,
#  'created_at': '2022-06-16T01:39:29.000Z',
#  'id': 4713988142,
#  'market_buy_amount': '16000.0',
#  'order_type': 'market_buy',
#  'pair': 'btc_jpy',
#  'rate': None,
#  'stop_loss_rate': None,
#  'success': True}