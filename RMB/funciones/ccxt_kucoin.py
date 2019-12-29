# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 18:10:19 2019

@author: MPAZ

INSTANCIA CON KUCOIN PARA SACAR ORDENES Y GENERAR UN CSV DE TRADES HECHAS


"""

import ccxt
from claves import api_key_kucoin,secret_kucoin

exchange_id='kucoin'
exchange_class=getattr(ccxt, exchange_id)
exchange = exchange_class({
        'apiKey': api_key_kucoin,
        'secret': secret_kucoin,
        'timeout': 30000,
        'enableRateLimit': True,
})


kucoin=ccxt.kucoin()
markets=kucoin.load_markets()
#print (kucoin.id, markets)

prueba=kucoin.fetch_trades('ETH/BTC')
import pprint

print (prueba)
