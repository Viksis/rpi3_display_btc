import json
import requests
import time
import os, sys
btc = "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT"
eth = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
xmr = "https://api.binance.com/api/v3/ticker/price?symbol=XMRUSDT"
ltc = "https://api.binance.com/api/v3/ticker/price?symbol=LTCUSDT"
sol = "https://api.binance.com/api/v3/ticker/price?symbol=SOLUSDT"
bnb = "https://api.binance.com/api/v3/ticker/price?symbol=BNBUSDT"
top = "#" * 60
left = "#\n"*17
left = "#" + " "*58 + "#" 
left = left * 15
left2 = "#" + " "*58 + "#" 
left2 = left2 * 16

def get_price(cryptopare):
        data = requests.get(cryptopare)
        data = data.json()
        price = f"{data['symbol']} {data['price']}"
        return price


os.system("clear")
while True:
        btc_price = get_price(btc)
        eth_price = get_price(eth)
        xmr_price = get_price(xmr)
        ltc_price = get_price(ltc)
        sol_price = get_price(sol)
        bnb_price = get_price(bnb)
        # os.system("clear")
        print(top)
        print(left)
        print("#" + " "*17, btc_price, " "*17 + "#")
        print("#" + " "*17, eth_price, " "*18 + "#")
        print("#" + " "*18, xmr_price, " "*18 + "#")
        print("#" + " "*18, ltc_price, " "*19 + "#")
        print("#" + " "*18, sol_price, " "*19 + "#")
        print("#" + " "*18, bnb_price, " "*18 + "#")
        print(left2)
        print("#"*60)
        # time.sleep(0.5)
