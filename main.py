# Lessun13 ボリンジャーバンド算出と、売り買い判断ロジック
# ライブラリのインポート
import configparser
import time

import pandas as pd

from coincheck import Coincheck

conf = configparser.ConfigParser()
conf.read("config.ini")

ACCESS_KEY = conf["coincheck"]["access_key"]
SERCRET_KEY = conf["coincheck"]["sercret_key"]

coincheck = Coincheck(access_key=ACCESS_KEY,sercret_key=SERCRET_KEY)
interval = 1
duration = 20
df = pd.DataFrame()

# BTCの最新価格を取得し続ける
while True:
    time.sleep(interval)
    # df = df.append({"price": coincheck.last}, ignore_index=True)
    d = {"price": coincheck.last}
    df_t = pd.DataFrame.from_dict(d,orient='index').T
    df = pd.concat([df,df_t], ignore_index=True)

    # 初期化完了判定
    if len(df) < duration:
        continue

    # ボリンジャーバンドを計算する
    df["SMA"] =df["price"].rolling(window=duration).mean()
    df["std"] =df["price"].rolling(window=duration).std()

    df["-2σ"] = df["SMA"] - 2*df["std"]
    df["+2σ"] = df["SMA"] + 2*df["std"]

    # 買いと売りの条件だけ書く
    if df["price"].iloc[-1] < df["-2σ"].iloc[-1]:
        print("buy!!!")
    if df["price"].iloc[-1] > df["+2σ"].iloc[-1]:
        print("Sell!!!")
