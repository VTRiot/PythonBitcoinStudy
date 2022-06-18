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
interval = 60 * 10
duration = 20
AMOUNT = 0.005
df = pd.DataFrame()

# BTCの最新価格を取得し続ける
while True:
    time.sleep(interval)
    position = coincheck.position

    if not position.get("jpy"):
        raise

    # df = df.append({"price": coincheck.last}, ignore_index=True)
    d = {"price": coincheck.last}
    df_t = pd.DataFrame.from_dict(d,orient='index').T
    df = pd.concat([df,df_t], ignore_index=True)

    # print(df)
    # 初期化完了判定
    if len(df) < duration:
        continue

    # ボリンジャーバンドを計算する
    df["SMA"] =df["price"].rolling(window=duration).mean()
    df["std"] =df["price"].rolling(window=duration).std()

    df["-2σ"] = df["SMA"] - 2*df["std"]
    df["+2σ"] = df["SMA"] + 2*df["std"]

    # 買いと売りの条件だけ書く
    if "btc" in position.keys():
        if df["price"].iloc[-1] > df["+2σ"].iloc[-1] \
            and coincheck.ask_rate < df["price"].iloc[-1]:

            params = {
                "order_type":"market_sell",
                "pair" :"btc_jpy",
                "market_buy_amount":position["btc"]
            }
            r = coincheck.order(params)
            print(r)
            print("Sell!!!")

    else:
        if df["price"].iloc[-1] < df["-2σ"].iloc[-1]:
            market_buy_amount = coincheck.rate({"order_type":"buy",
                                                "pair":"btc_jpy",
                                                "amount":AMOUNT})
            params = {
                "order_type":"market_buy",
                "pair" :"btc_jpy",
                "market_buy_amount":market_buy_amount["price"]
            }
            r = coincheck.order(params)
            print(r)
            print("buy!!!")
