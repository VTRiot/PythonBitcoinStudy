 # Lessun11plus Ticker以外を自前でClass化トライ
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

    #order_books板情報の取得
    def order_books(self):
        endpoint = self.url + "/api/order_books"
        limit_num = 5
        params = {
            "limit":limit_num   
        }
        return self._request(endpoint=endpoint,params=params)
    #trades
    def trades(self, params):
        endpoint = self.url + '/api/trades'
        return self._request(endpoint=endpoint, params=params)    
    
    #balance
    def balance(self):
        endpoint = self.url + '/api/accounts/balance'
        return self._request(endpoint=endpoint)

    #order
    def order(self, params):
        endpoint = self.url + '/api/exchange/orders'
        return self._request(endpoint=endpoint, params=params, method='POST')
