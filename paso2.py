import ccxt
import time
import shelve
import pandas as pd

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
