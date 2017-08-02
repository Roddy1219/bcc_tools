#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import decimal
import hashlib
import json
import time
import requests
from datetime import datetime, timezone, timedelta

def main():
    while True:
        try:
            resp = requests.get(url='https://www.okex.com/v2/markets/tickers', timeout=10)
            result = json.loads(resp.text)

            ok_bcc_btc_price = round(float(result['data'][0]['last']), 4)

            # 火币的api是我见过的最烂的api，命名垃圾，居然api反爬虫，可见火币的技术内部混乱随意垃圾！！！！
            headers = { "Accept":"text/html,application/xhtml+xml,application/xml;",
                        "Accept-Encoding":"gzip",
                        "Accept-Language":"zh-CN,zh;q=0.8",
                        "Referer":"http://www.example.com/",
                        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.90 Safari/537.36" }

            resp = requests.get(url='https://api.huobi.pro/market/detail/merged?symbol=bccbtc', headers=headers, timeout=10)
            result = json.loads(resp.text)
            hb_bcc_btc_price = round(float(result['tick']['close']), 4)


            resp = requests.get(url='https://www.okcoin.cn/api/v1/ticker.do?symbol=btc_cny', timeout=10)
            result = json.loads(resp.text)

            ok_btc_cny_price = float(result['ticker']['last'])

            hb_btc_cny_price = round(hb_bcc_btc_price*ok_btc_cny_price, 2)

            ok_bcc_cny_price = round(ok_bcc_btc_price*ok_btc_cny_price, 2)

            resp = requests.get(url='http://www.jubi.com/api/v1/allticker/', timeout=10)
            result = json.loads(resp.text)

            jb_bcc_cny_price = round(float(result['bcc']['last']),2)


            resp = requests.get(url='https://www.viabtc.com/api/v1/market/ticker?market=BCCCNY', timeout=10)
            result = json.loads(resp.text)
            vb_btc_cny_price = round(float(result['data']['ticker']['last']), 2)


            now = datetime.now() # 获取当前datetime
            print(now)
            print("BCC_BTC:ok_bcc_btc_price, hb_bcc_btc_price:", ok_bcc_btc_price, hb_bcc_btc_price)

            print("BCC_CNY:ok_btc_cny_price, hb_btc_cny_price, ok_bcc_cny_price, vb_btc_cny_price, jb_bcc_cny_price:", ok_btc_cny_price, hb_btc_cny_price, ok_bcc_cny_price, vb_btc_cny_price, jb_bcc_cny_price)
        except Exception as identifier:
            print(identifier)

        time.sleep(1)


if __name__ == '__main__':
    main()
