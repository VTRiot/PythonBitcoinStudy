# Lessun11 成り行き売り
# ライブラリのインポート
import configparser
from coincheck import Coincheck

conf = configparser.ConfigParser()
conf.read("config.ini")

ACCESS_KEY = conf["coincheck"]["access_key"]
SERCRET_KEY = conf["coincheck"]["sercret_key"]

coincheck = Coincheck(access_key=ACCESS_KEY,sercret_key=SERCRET_KEY)
# ticker = coincheck.ticker()
# print(ticker)

print(coincheck.last)