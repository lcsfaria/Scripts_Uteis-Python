import pandas as pd
arq = open('C:\\Users\\lucasf\\Desktop\\arquivoInicial.txt','r')
vet = []
for i in arq:
    vet.append(i.split())
df = pd.DataFrame(vet)
df.to_csv('C:\\Users\\lucasf\\Desktop\\arquivoFinal.txt', sep='\t', index=False, header=0)
