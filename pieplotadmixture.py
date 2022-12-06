"""
2022
@author: lucasf
"""

import pandas as pd

arq = open('C:\\Users\\lucasf\\Desktop\\2escolhe_K5.txt','r')
vet = []
for i in arq:
    vet.append(i.split())

intermediario = pd.DataFrame(vet, columns=vet[0])
dados= intermediario.iloc[1:,:]

dados[['C1', 'C2', 'C3', 'NAT', 'C5']] = dados[['C1', 'C2', 'C3', 'NAT', 'C5']].astype(float)

pops = []

for i in dados['POP']:
    pops.append(i)

pops = set(pops)
#pops = list(pops)

total =[]
for i in pops:
    filtro= dados.loc[dados['POP']==i]
    k1 = filtro['C1'].mean()
    k2 = filtro['C2'].mean()
    k3 = filtro['C3'].mean()
    nat = filtro['NAT'].mean()
    k5 = filtro['C5'].mean()

    valores = [i,k1,k2,k3,nat,k5]
    total.append(valores)

df = pd.DataFrame(total, columns=['POP','C1_mean','C2_mean','C3 mean','NAT_mean','C5_mean'])
df.to_csv('C:\\Users\\lucasf\\Desktop\\meank5.txt', sep='\t',index= False )

###############################################################################################

valores= pd.read_csv('C:\\Users\\lucasf\\Desktop\\meank5.txt', sep='\t')

valores=valores.dropna()
valores


###############################################################################################

tr=valores.T

tr.to_csv('C:\\Users\\lucasf\\Desktop\\transpostomeank5.txt', sep='\t')
data= pd.read_csv('C:\\Users\\lucasf\\Desktop\\transpostomeank5.txt', sep='\t', header=1)

nomes=list(data.columns[1:])
indexa=[['Jacarus', 1], ['Chopccas', 2], ['Quechuas', 3], ['Qeros', 4], ['Puno', 5], ['Uros', 6], ['Tallanes', 7], ['Moche', 8], ['Chachapoyas', 9], ['Awajun', 10], ['Candoshi', 11], ['Lamas', 12], ['Matses', 13], ['Shipibo', 14], ['Ashaninkas', 15], ['Matsiguenkas', 16]]



###############################################################################################


for i in nomes:
    fig1 = plt.figure()
    plt.pie(data[i], colors=["#556B2F","yellowgreen","red","#cd8500","blue"])
    plt.scatter( 0 , 0 , s = 6000, color='black')
    tenta= [j[1] for j in indexa if i in j]
    if len(tenta)==1 and tenta[0]>9:
        plt.text(-0.3,-0.150, tenta[0],color='white',fontsize=50)
    elif len(tenta)==1 and tenta[0]<=9:
        plt.text(-0.130,-0.17, tenta[0],color='white',fontsize=50)
    plt.title(i,fontsize=30)
    fig1.savefig(f'C:\\Users\\lucasf\\Desktop\\testes\\{i}Plot.pdf')


######################################### Plotar com valores ######################################################

nomes=list(data.columns[1:])
indexa=[['Jacarus', 1], ['Chopccas', 2], ['Quechuas', 3], ['Qeros', 4], ['Puno', 5], ['Uros', 6], ['Tallanes', 7], ['Moche', 8], ['Chachapoyas', 9], ['Awajun', 10], ['Candoshi', 11], ['Lamas', 12], ['Matses', 13], ['Shipibo', 14], ['Ashaninkas', 15], ['Matsiguenkas', 16]]


for i in nomes:
    popi=data[i].tolist()
    va= data[i].tolist()
    fig1 = plt.figure()
    plt.pie(data[i], colors=["#556B2F","yellowgreen","red","#cd8500","blue"],labels=va)
    plt.scatter( 0 , 0 , s = 6000, color='black')
    tenta= [j[1] for j in indexa if i in j]
    if len(tenta)==1 and tenta[0]>9:
        plt.text(-0.3,-0.150, tenta[0],color='white',fontsize=50)
    elif len(tenta)==1 and tenta[0]<=9:
        plt.text(-0.130,-0.17, tenta[0],color='white',fontsize=50)
    plt.title(i,fontsize=30)
    fig1.savefig(f'C:\\Users\\lucasf\\Desktop\\valores\\{i}Plot.pdf')


###############################################################################################

fig1 = plt.figure()
plt.pie(data['Shimaa'], colors=["#556B2F","yellowgreen","red","#cd8500","blue"])
plt.scatter( 0 , 0 , s = 6000, color='black')
plt.text(-0.32,-0.13,'16B',color='white',fontsize=35)
plt.title('Matsiguenkas',fontsize=30)
fig1.savefig(f'C:\\Users\\lucasf\\Desktop\\testes\\MatsiguenkasBPlot.pdf')


popi=data.POP.tolist()
va= data.Aimaras.tolist()


###############################################################################################
fig1 = plt.figure()

popi=data.POP.tolist()
va= data.Shimaa.tolist()
plt.pie(data['Shimaa'], colors=["#556B2F","yellowgreen","red","#cd8500","blue"],labels=va)
plt.scatter( 0 , 0 , s = 6000, color='black')
plt.text(-0.32,-0.13,'16B',color='white',fontsize=35)
plt.title('Matsiguenkas',fontsize=30)
fig1.savefig(f'C:\\Users\\lucasf\\Desktop\\valores\\MatsiguenkasBPlot.pdf')


###############################################################################################
fig1 = plt.figure()
va= data.Matsiguenkas.tolist()
plt.pie(data['Matsiguenkas'], colors=["#556B2F","yellowgreen","red","#cd8500","blue"])
plt.scatter( 0 , 0 , s = 6000, color='black')
plt.text(-0.32,-0.13,'16A',color='white',fontsize=35)
plt.title('Matsiguenkas',fontsize=30)
fig1.savefig(f'C:\\Users\\lucasf\\Desktop\\testes\\MatsiguenkasAPlot.pdf')


###############################################################################################
fig1 = plt.figure()
va= data.Aimaras.tolist()
popi=data.POP.tolist()
plt.pie(data['Aimaras'], colors=["#556B2F","yellowgreen","red","#cd8500","blue"],labels=popi)
plt.scatter( 0 , 0 , s = 6000, color='black')
plt.text(-0.130,-0.17,5,color='white',fontsize=50)
plt.title('Puno',fontsize=30)
#fig1.savefig(f'C:\\Users\\lucasf\\Desktop\\valores\\PunoPlot.pdf')


###############################################################################################

import plotly.graph_objects as go

popi=data.POP.tolist()
va= data.Aimaras.tolist()
fig1 = plt.figure()
plt.pie(data['Aimaras'], colors=["#556B2F","yellowgreen","red","#cd8500","blue"],labels=va)
plt.scatter( 0 , 0 , s = 6000, color='black')
plt.text(-0.130,-0.17,5,color='white',fontsize=50)
plt.title('Puno',fontsize=30)
fig1.savefig(f'C:\\Users\\lucasf\\Desktop\\teste\\PunoPlot.pdf')

