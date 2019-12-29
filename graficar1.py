# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:18:37 2019

@author: MPAZ
"""

import ccxt
from funciones.claves import api_key, secret
import pandas as pd
import matplotlib.pyplot as plt

# INSTANCIA CON BINANCE
exchange_id = 'binance'
exchange_class = getattr(ccxt, exchange_id)
binance = exchange_class({
    'apiKey': api_key,
    'secret': secret,
    'timeout': 30000,
    'enableRateLimit': True,
})

mercados = binance.load_markets(True)

monedas = binance.currencies

pares = binance.symbols

metodos = dir(binance)

saldo = binance.balance

# par='ADA/ETH'

print("EMPEZAMOS!")


def dibujar(par):

    ohlcv = binance.fetch_ohlcv(par, '1d')
    df = pd.DataFrame(ohlcv, columns=['Fecha',
                                      'Open',
                                      'High',
                                      'Lowest',
                                      'Closing',
                                      'Volumen'])

    df['Fecha'] = pd.to_datetime(df['Fecha'], unit='ms')
    df['Volatilidad'] = df['High'] - df['Lowest']
    df['%'] = df['Volatilidad'] / df['Open'] * 100
    df['%'] = df['%'].round(decimals=1)
    miniserie = df['%'][-10:-1]
    col_list = list(df)
    # plt.figure()
    plt.title(par)
    plt.plot(miniserie, 'g')
    plt.xlabel('DIAS ULTIMA SEMANA')
    plt.ylabel('%VOLATILIDAD PRECIO DIARIA')
    plt.axhline(3, color='b')
    plt.ylim(0, 10)
    plt.text
    plt.axhspan(5, 8, alpha=0.25, color='red')
    plt.legend()
    plt.show()


pares_mini = pares[0:2]

volatilidades = {}

for par in pares_mini:
    dibujar(par)
    volatilidades[par] = 2
