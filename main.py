# Lessun9 指値注文
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
    "order_type" : "buy",
    "rate" : 3_000_000,
    "amount" : 0.005
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
