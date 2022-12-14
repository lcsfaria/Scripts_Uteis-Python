"""
2022
@author: lucasf
"""
import pandas as pd

file1 = pd.read_csv('/home/lucasf/', sep='\t')
file2 = pd.read_csv('/home/lucasf/', sep='\t')

juntos = pd.merge(file1, file2, on='ID', how='inner') #em 'on' escolha qual vai ser a coluna de verificar a intersecao, 'how' é para fazer a intersecao

juntos1 = juntos.drop(columns=['Unnamed: 0'])

juntos2 = juntos1.rename(columns={'Pop_y':'Pop'})

juntos2.to_csv('/home/lucasf/file3', sep='\t', header=True, index=None)

## nao eh necessario criar juntos1 e juntos 2, poderiamos realizar todas as operacoes no mesmo lugar, mas ter o arquivo de um passo anterior eh sempre bom
