# Lessun8
# ライブラリのインポート
import configparser
import hmac
import hashlib
from pprint import pprint
import time

import requests

conf = configparser.ConfigParser()
conf.read("config.ini")

ACCESS_KEY = conf["coincheck"]["access_key"]
SERCRET_KEY = conf["coincheck"]["sercret_key"]

# URLの設定
BASE_URL = "https://coincheck.com"
url = BASE_URL + "/api/accounts/balance"

nonce = str(int(time.time()))

body = ""
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

# 情報を取得する
# params = {
#     "limit": 5
# }

# r = requests.get(url, params=params)
r = requests.get(url, headers=headers)
r = r.json()
# pprint(r["asks"][::-1])
# pprint(r["bids"])
pprint(r)
