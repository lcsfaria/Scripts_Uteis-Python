"""
2022
@author: lucasf
"""

import pandas as pd
dados = pd.read_csv('C:\\Users\\lucasf\\home', sep='\t')
pops = []

#Como os nomes das pop se repetem, pegamos o nome de todas uma unica vez
for i in dados['Pop']:
    pops.append(i)

pops = set(pops)

#aqui agrupamos elas e jah calculamos a mehdia de cada K, no caso temos 4 colunas que queremos sabe as medias: coluna K1, K2,K3 e K4

total =[]
for i in pops:
    filtro= dados.loc[dados['Pop']==i]
    k1 = filtro['K1'].mean()
    k2 = filtro['K2'].mean()
    k3 = filtro['K3'].mean()
    k4 = filtro['K4'].mean()

    valores = [i,k1,k2,k3,k4]
    total.append(valores)

df = pd.DataFrame(total, columns=['Pop','k1 mean','k2 mean','k3 mean','k4 mean'])
df.to_csv('C:\\Users\\lucasf\\Desktop\\Dadosluca.txt', sep='\t',index= False )
