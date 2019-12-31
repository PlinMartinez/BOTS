# -*- coding: utf-8 -*-
"""
Created on Tue Dec 31 10:21:26 2019

@author: MPAZ
"""

import shelve
import ccxt
from funciones.claves import api_key_binance,secret_binance
import pandas as pd
import time


db=shelve.open('tablas')
par=db['pares_vivos']

pares=par[0:10]

# INSTANCIAR POR PASOS
binance=ccxt.binance()
binance.apiKey=api_key_binance
binance.secret=secret_binance
binance.timeout=30000
binance.enableRateLimit=True

mercados = binance.load_markets(True)


par2 = 'ETH/BTC'

while True:
    

    def ordenar_df1(par):
        ordenes=binance.fetch_trades(par2)
        df=pd.DataFrame(ordenes)
        del [df['info'],df['order'],df['type'],df['symbol']]
        del [df['takerOrMaker'],df['fee']]
        df['fecha']=pd.to_datetime(df['timestamp'],unit='ms')
        del [df['timestamp'],df['datetime'],df['side'],df['amount'],df['cost']]
        df.columns=['id','precio','fecha']
        return df
    
    df=ordenar_df1(par2)
    
    
    def ordenar_df2(df):
        '''AGRUPAR POR MINUTOS EL DATAFRAME , SACAR MIN Y MAX'''
        df = df.set_index('fecha')
        ordenes = df['id'].resample('1min').count()
        minimo = df['precio'].resample('1min').min()
        maximo = df['precio'].resample('1min').max()
        media = df['precio'].resample('1min').mean()
        variacion = round((maximo - minimo) / minimo * 100, 1)
        ultimo = df['precio'].resample('1min').last()
        series = [ordenes, minimo, maximo, media, variacion, ultimo]
        df2 = pd.DataFrame(series)
        df2 = df2.T
        df2.columns = ['ordenes', 'minimo',
                       'maximo', 'media', 'variacion', 'ultimo']
        return df2
    
    df= ordenar_df2(df)
    
    antes=df.iloc[-3,3]
    media=df.iloc[-2,3]
    despues=df.iloc[-1,3]
    
    libro_ordenes = binance.fetch_order_book(par2, 100)
    ask=libro_ordenes['asks'][0][0]
    bid=libro_ordenes['bids'][0][0]
    spread=ask-bid
    spread_porcentaje=round(spread/bid*100,1)
    spread_medio=(ask+bid)/2
    spread_min=spread_medio*0.995
    spread_max=spread_medio*1.005
    
    minimo_notional = float(mercados[par2]['info']['filters'][3]['minNotional'])
    precision=mercados[par2]['precision']
    precision_amount=precision['amount']
    precision_price=precision['price']
    q_compra=minimo_notional/spread_min*1.2
    q_venta=minimo_notional/spread_max*1.2
    
    '''
    symbol = par2
    type = 'limit'
    side = 'buy'
    amount = round(q_compra,precision_amount)
    price=round(spread_min,precision_price)
    total=amount*price
    
    
    orden=binance.create_order(symbol,type,side,amount,price)
    print('hecha orden de compra ' + symbol)
    
    symbol = par2
    type = 'limit'
    side = 'sell'
    amount = round(q_compra,precision_amount)
    price=round(spread_max,precision_price)
    total=amount*price
    
    
    orden=binance.create_order(symbol,type,side,amount,price)
    print('hecha orden de venta ' + symbol)
    '''
    
    
    if media > antes and media >despues:
        print ("vende")
        symbol = par2
        type = 'limit'
        side = 'sell'
        amount = round(q_compra,precision_amount)
        price=round(spread_max,precision_price)
        total=amount*price
        
        
        orden=binance.create_order(symbol,type,side,amount,price)
        print('hecha orden de venta ' + symbol)
        
    if media < antes and media < despues:
        print ("compra")
        symbol = par2
        type = 'limit'
        side = 'buy'
        amount = round(q_compra,precision_amount)
        price=round(spread_min,precision_price)
        total=amount*price
        
        
        orden=binance.create_order(symbol,type,side,amount,price)
        print('hecha orden de compra ' + symbol)
    
    print ('A dormir 45 segundos')
    time.sleep(45)
    
        


