# -*- coding: utf-8 -*-
"""
Created on Thu Dec 19 07:46:53 2019

@author: MPAZ
"""

import ccxt
import pandas as pd

# INSTANCIA CON BINANCE
exchange_id='binance'
exchange_class=getattr(ccxt, exchange_id)
binance =exchange_class({
        'apiKey':api_key,
        'secret':secret,
        'timeout':30000,
        'enableRateLimit': True,
})

mercados=binance.load_markets(True)
monedas=binance.currencies
pares=binance.symbols



