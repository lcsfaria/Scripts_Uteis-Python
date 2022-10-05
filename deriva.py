"""
2022
@author: lucasf
"""

import random as rd

alelos = ['a','b','c','d','e']
pop0 = []

for i in range(10):#numero de indivduos da pop
    pop0.append(rd.choice(alelos))
for i in alelos:
    print('frequencia inicial de',i,pop0.count(i))

popf = [pop0]

for i in range(99999999):#numero de vezes que irá rodar
    
    popinter = []
    for j in range(10):
        popinter.append(rd.choice(popf[-1]))
    
    popf.extend([popinter])

    fix= set(popf[-1])
    if len(fix)==1:
        print(f'Demorou {i} geracoes para fixar\n')
        break    

for i in popf:
    print(i)
