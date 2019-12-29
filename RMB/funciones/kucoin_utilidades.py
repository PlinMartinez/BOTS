# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 17:39:49 2019

@author: MPAZ
"""

import time
import base64
import hmac
import hashlib
import requests

#Example for get balance of accounts in python

api_key = "5dffa2a9a7eb410009817ac7"
api_secret = "bed03edd-6d11-4207-bfd4-ca5b7ad08369"
api_passphrase = "bed03edd-6d11-4207-bfd4-ca5b7ad08369"
url = 'https://openapi-sandbox.kucoin.com/api/v1/accounts'
now = int(time.time() * 1000)
str_to_sign = str(now) + 'GET' + '/api/v1/accounts'
signature = base64.b64encode(
    hmac.new(api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
headers = {
    "KC-API-SIGN": signature,
    "KC-API-TIMESTAMP": str(now),
    "KC-API-KEY": api_key,
    "KC-API-PASSPHRASE": api_passphrase
}
response = requests.request('get', url, headers=headers)
print(response.status_code)
print(response.json())


'''
 #Example for create deposit addresses in python
url = 'https://openapi-sandbox.kucoin.com/api/v1/deposit-addresses'
now = int(time.time() * 1000)
data = {"currency": "BTC"}
data_json = json.dumps(data)
str_to_sign = str(now) + 'POST' + '/api/v1/deposit-addresses' + data_json
signature = base64.b64encode(
    hmac.new(api_secret.encode('utf-8'), str_to_sign.encode('utf-8'), hashlib.sha256).digest())
headers = {
    "KC-API-SIGN": signature,
    "KC-API-TIMESTAMP": str(now),
    "KC-API-KEY": api_key,
    "KC-API-PASSPHRASE": api_passphrase,
    "Content-Type": "application/json" # specifying content type or using json=data in request
}
response = requests.request('post', url, headers=headers, data=data_json)
print(response.status_code)
print(response.json())
'''
