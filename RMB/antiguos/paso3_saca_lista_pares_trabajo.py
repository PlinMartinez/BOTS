# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 23:19:58 2019

@author: MPAZ

SACA pares_vivos mezclando las 2 tablas para tener una lista con
volatilidad > 3%
ordenes > 500 / hora


"""

import ccxt
import shelve

binance=ccxt.binance()

mercados=binance.load_markets()

pares=binance.symbols

obj=shelve.open('tablas')

pares_vivos_velocidad=obj['pares_vivos_velocidad']
pares_vivos_amplitud=obj['pares_vivos_amplitud']

pares_vivos=[]

for item in pares_vivos_velocidad:
    print (item)
    if item in pares_vivos_amplitud:
        pares_vivos.append(item)

obj=shelve.open('tablas')
obj['pares_vivos']=pares_vivos

print ('La lista de pares vivos es la siguiente '+str(len(pares_vivos)))
print (pares_vivos)

 