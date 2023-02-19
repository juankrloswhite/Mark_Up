import pandas as pd
import numpy as np
import time
from datetime import datetime 

#Contador tiempo de inicio del cod
inicio = time.time()

path = 'BrandedFaresTickets.csv'
df = pd.read_csv(path, sep= ';') 
print(df.head(5))

FARE_CLASS = ['I','R','G','X','N']

## Filtra  IT_FAre = N
mask = df['ITFARE'] == 'N'
df = df[mask]

## Filtro FARE_CLASS
df = df[(df['FARE_CLASS'] != 'I') & (df['FARE_CLASS'] != 'R') & (df['FARE_CLASS'] != 'G')& (df['FARE_CLASS'] != 'X')& (df['FARE_CLASS'] != 'N')]

## Cambiar a formato fecha
df['DAIS'] = pd.to_datetime(df['DAIS'], format='%Y%m%d') #Convertir a formato fecha
#df['ODFTDA'] = pd.to_datetime(df['ODFTDA'], format='%Y%m%d')

##Calculo de la semana, año y mes
df['WEEK'] = df['DAIS'].dt.strftime('%V')
df['YYYY'] = df['DAIS'].dt.strftime('%Y')
df['MONTH'] = df['DAIS'].dt.strftime('%m')

print(df['ODFTDA'])
#print(type(df.info()))
#print(dfclean['FARE_CLASS'].unique())
#print(df.columns.values)

#Contador tiempo final del cod
fin = time.time()
print(fin-inicio)



