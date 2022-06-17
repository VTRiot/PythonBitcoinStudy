 # Lessun11 共通処理をクラス化する
 # ライブラリのインポート
import hmac
import hashlib
import json
import time

import requests

class Coincheck(object):
    def __init__(self, access_key, sercret_key):
        self.access_key = access_key
        self.sercret_key = sercret_key
        self.url = "https://coincheck.com"

    def _request(self,endpoint,params = None, method = "GET"):
        nonce = str(int(time.time()))

        if params == None:
            body = ""
        else:
            body = json.dumps(params)
        message = nonce + endpoint + body

        signature = hmac.new(self.sercret_key.encode(),
                            message.encode(),
                            hashlib.sha256).hexdigest()

        headers = {
            "ACCESS-KEY": self.access_key,
            "ACCESS-NONCE": nonce,
            "ACCESS-SIGNATURE": signature,
            "Content-Type": "application/json"
        }

        if method == "GET":
            r = requests.get(endpoint, headers=headers,params=params)
        else:
            r = requests.post(endpoint, headers=headers,data=body)
        return r.json()

    #Ticker
    def ticker(self):
        endpoint = self.url + "/api/ticker"
        return self._request(endpoint=endpoint)

    @property
    def last(self):
        return self.ticker()["last"]

    #order_books
    #trades
    #balance
    #order
    