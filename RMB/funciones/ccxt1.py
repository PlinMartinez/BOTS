# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:53:10 2019

@author: MPAZ
"""

import ccxt
from claves import api_key_binance,secret_binance

mercados=binance.load_markets(True)

pares= binance.currencies

monedas=binance.currencies

metodods=dir(binance)

saldo=binance.balance


def instanciar():
    # INSTANCIA CON BINANCE
    exchange_id='binance'
    exchange_class=getattr(ccxt, exchange_id)
    binance =exchange_class({
            'apiKey':api_key_binance,
            'secret':secret_binance,
            'timeout':30000,
            'enableRateLimit': True,
    })
    return binance



