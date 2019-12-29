# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 10:18:37 2019

@author: MPAZ
"""

import pandas as pd
import matplotlib.pyplot as plt


fichero='20191218ADAETH.csv'
df=pd.read_csv(fichero)

df['fecha']=pd.to_datetime(df['fecha'])
del [df['timestamp'], df['Unnamed: 0']]



'''AGRUPAR POR MINUTOS EL DATAFRAME , SACAR MIN Y MAX'''
df=df.set_index('fecha')
ordenes=df['id'].resample('30min').count()
minimo=df['precio'].resample('30min').min()
maximo=df['precio'].resample('30min').max()
media=df['precio'].resample('30min').mean()
variacion=round((maximo-minimo)/minimo*100,1)
ultimo=df['precio'].resample('30min').last()
series=[ordenes,minimo,maximo,media,variacion,ultimo]    
df2=pd.DataFrame(series)
df2=df2.T
df2.columns=['ordenes','minimo','maximo','media','variacion','ultimo']
'''
df2.drop(['minimo','maximo','variacion','ultimo'],axis='columns',inplace=True)

plt.plot(df2,'g')

plt.title('ADA/BTC')

plt.xlabel('horas')
plt.ylabel('precio')
'''
df2.media=df2.media.shift(1)

ax=df2['minimo'].plot()
ax=df2['maximo'].plot()
ax=df2.ordenes.plot(secondary_y=True, label="Comments", legend=True) 



