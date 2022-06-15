#Lessun5
#ライブラリのインポート
from pprint import pprint
import requests

#URLの設定
BASE_URL = "https://coincheck.com" 
url = BASE_URL + "/api/trades"
# ed_id = 221771450
# st_id = ed_id + 10

#情報を取得する
params = {
    "pair":"btc_jpy",
    # "ending_before":ed_id,
    # "starting_after":st_id
    "limit":100
    
}
r = requests.get(url,params=params).json()
#r = r.json()
pprint(r)