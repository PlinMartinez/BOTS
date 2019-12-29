# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 21:29:19 2019

@author: MPAZ

MIRA TODOS LOS PARES DE UN EXCHANGE Y CLASIFICA

SI LAS ULTIMAS 500 ORDENES HECHAS > 24 HORAS EL MERCADO ESTA MUERTO
SI LAS ULTIMAS 500 ORDENES HECHAS < 1 HOR EL MERCADO ESTA VIVO Y SE PUEDE NAVEGAR

Pasa a Shelve estos 2 listados para futuros trabajos
pares_vivos_velocidad
pares_muertos_velocidad
SACA LOS OHLCV de cada par y agrupa
si volatilidad <1% >> mercado mueto
si volatlidad >3% >> mercado jugoso

"""

import ccxt
import time
import shelve
import pandas as pd

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

binance=ccxt.binance()

mercados=binance.load_markets()

pares=binance.symbols

mini_pares=pares[0:3]

volatilidad={}

for par in pares:
    
    print('Empezamos a mirar OHLCV con el par '+par)
    ohlcv=binance.fetch_ohlcv(par,'1d')
    df=pd.DataFrame(ohlcv)
    df.columns=['time','open','high','low','close','volume']
    df['time']=pd.to_datetime(df['time'],unit='ms')
    df=df.set_index('time')
    df['volatilidad']=round((df['high']-df['low'])/df['low']*100,1)
    ayer=df['volatilidad'][-2]
    volatilidad[par]=ayer
    time.sleep(2)
    
    
pares_vivos_amplitud=[]
pares_muertos_amplitud=[]

for clave,valor in volatilidad.items():
    if valor<1:
        pares_muertos_amplitud.append(clave)
    if valor>3:
        pares_vivos_amplitud.append(clave)
        
    
obj=shelve.open('tablas')
obj['pares_vivos_amplitud']=pares_vivos_amplitud
obj['pares_muertos_amplitud']=pares_muertos_amplitud
obj.close


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