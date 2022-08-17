import pandas as pd
arq = open('C:\\Users\\lucasf\\Desktop\\novo 1.txt','r')
vet = []
for i in arq:
    vet.append(i.split())
df = pd.DataFrame(vet2)
df.to_csv('C:\\Users\\lucasf\\Desktop\\novo 2.txt', sep='\t', index=False, header=0)
