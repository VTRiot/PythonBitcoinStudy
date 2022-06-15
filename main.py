#Lessun6
#ライブラリのインポート
from pprint import pprint
import requests

#URLの設定
BASE_URL = "https://coincheck.com" 
url = BASE_URL + "/api/order_books"

#情報を取得する
params = {
    "limit":5   
}

r = requests.get(url,params=params)
r = r.json()
pprint(r["asks"][::-1])
pprint(r["bids"])