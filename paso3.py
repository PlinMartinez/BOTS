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

 
