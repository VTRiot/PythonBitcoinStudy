#ライブラリのインポート
from pprint import pprint
import requests

#URLの設定
BASE_URL = "https://coincheck.com" 
url = BASE_URL + "/api/ticker"


#情報を取得する
r = requests.get(url)
r = r.json()
print(r["high"])