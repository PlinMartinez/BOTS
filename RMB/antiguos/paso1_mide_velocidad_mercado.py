# -*- coding: utf-8 -*-
"""
Created on Thu Dec 26 21:58:46 2019

@author: MPAZ


MIRA TODOS LOS PARES DE UN EXCHANGE Y CLASIFICA

SI LAS ULTIMAS 500 ORDENES HECHAS > 24 HORAS EL MERCADO ESTA MUERTO
SI LAS ULTIMAS 500 ORDENES HECHAS < 1 HOR EL MERCADO ESTA VIVO Y SE PUEDE NAVEGAR

Pasa a Shelve estos 2 listados para futuros trabajos
pares_vivos_velocidad
pares_muertos_velocidad


"""


import ccxt
import time
import shelve

binance=ccxt.binance()

mercados=binance.load_markets()

pares=binance.symbols

mini_pares=pares[0:3]

ordenes=binance.fetch_trades(mini_pares[0])
primero=ordenes[0]['timestamp']
ultimo=ordenes[-1]['timestamp']
delay=ultimo-primero
retraso=round(delay/(1000*60*60),1)

velocidad={}

for par in pares:
    try:
        print ('empieza con el par '+par)
        ordenes=binance.fetch_trades(par)
        primero=ordenes[0]['timestamp']
        ultimo=ordenes[-1]['timestamp']
        delay=ultimo-primero
        retraso=round(delay/(1000*60*60),1)
        velocidad[par]=retraso
        time.sleep(2)
    except:
        print ('el par este ha salido chungo'+par)


pares_vivos_velocidad=[]
pares_muertos_velocidad=[]

for clave,valor in velocidad.items():
    if valor<=1:
        pares_vivos_velocidad.append(clave)
    if valor>24:
        pares_muertos_velocidad.append(clave)
        
    
obj=shelve.open('tablas')
obj['pares_vivos_velocidad']=pares_vivos_velocidad
obj['pares_muertos_velocidad']=pares_muertos_velocidad
obj.close
