import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math

#tuda linha que comeca com # e um comentario
#os comentarios nao sao compilados, servem para explicar o codigo

#criacao de variaveis tipo lista, definidas pelo colchete
vx = [0,1,2,3,4,5]
vy = [5,6,7,8,9,10]

#criacao de variaveis tipo vetor numpy
ax = np.zeros(10)
ay = np.zeros(10)

#loop no qual i1 vai de 0 ate 10-1 = 9
for i1 in range(10):
    ax[i1] = i1+1
    ay[i1] = math.log(ax[i1]) 
    print(i1,',',ax[i1],',',ay[i1])

#fazendo o grafico
plt.plot(ax,ay) #cria o grafico
plt.xlabel('eixo x') #define o nome no eixo x
plt.ylabel('eixo y') #define o nome no eixo y
#plt.show()
#salvando a figura em um arquivo
plt.savefig('figura.png',dpi = 300, bbox_inches='tight')


