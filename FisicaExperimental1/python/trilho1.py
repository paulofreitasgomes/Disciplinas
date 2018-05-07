


#Este codigo grafica a posicao, velocidade e aceleracao em funcao do tempo a partir dos dados
#obtidos no experimento do trilho de ar

import numpy as np
import matplotlib.pyplot as plt
import pylab, math

#Importando os dados de posicao e tempo
tempop,posicao = np.loadtxt('posicao2.txt',usecols=[0,1],unpack=True);
tempov,velocidade = np.loadtxt('velocidade2.txt',usecols=[0,1],unpack=True);
tempoa,aceleracao = np.loadtxt('aceleracao2.txt',usecols=[0,1],unpack=True);



#Graficos
plt.subplot(3,1,1)
plt.title('Posicao, velocidade e aceleracao em funcao do tempo',fontsize=14)
plt.plot(tempop,posicao,'ob', ms = 5,label = 'posicao')
plt.legend(loc='upper left',fontsize=12)
#plt.yticks((-0.2, 0.7, 1.6), ('-0.2', '0.7', '1.6'))
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are off
plt.ylabel('$x$ (m)', {'color': 'k','fontsize': 16})
plt.grid(True)
plt.subplot(3,1,2)
plt.plot(tempov,velocidade,'ok', ms = 5, label = 'velocidade')
plt.grid(True)
plt.legend(loc='upper left',fontsize=12)
plt.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off') # labels along the bottom edge are off
#plt.yticks((-6, 0, 6), ('-6', '0', '6'))
plt.ylabel('$v$ (m/s)', {'color': 'k','fontsize': 16})
plt.subplot(3,1,3)
plt.plot(tempoa,aceleracao,'or', ms = 5, label = 'aceleracao')
plt.xlabel('Tempo $t$ (s)', {'color': 'k','fontsize': 18})
plt.grid(True)
plt.ylabel('$a$ (m/s$^2$)', {'color': 'k','fontsize': 16})
plt.xticks(color='k', size=16)
#plt.yticks((-200, 700, 1600), ('-200', '700', '1600'))
plt.legend(loc='lower right',fontsize=12)
plt.savefig('gtrilho.pdf',dpi=200)
#plt.show()
plt.close()


#Valores das massa do experimento 1 do grupo masculino
mtrilho = 418.3 #gramas
msuspenso = 10.0 #gramas
gravidade = 9.80 # metros por segundo ao quadrado



#erros nas massas
delta_suspenso = 0.5
delta_trilho = 0.5

deltay = delta_suspenso + delta_trilho

#o erro na divisao das massas sera
erro_massa = (msuspenso * deltay + (mtrilho + msuspenso) * delta_suspenso ) / (mtrilho + msuspenso) ** 2

# aceleracao teorica
ateorico = ( msuspenso * gravidade ) / (mtrilho + msuspenso)

#erro na aceleracao teorica sera
erro_aceleracao = gravidade * erro_massa

#Calculo da aceleracao media obtida no experimento

Nace = len(aceleracao) #numero de elementos no vetor aceleracao
soma = 0.0

for ind in xrange(Nace):
    soma += aceleracao[ind]

atmedio = soma / Nace

soma_quad = 0.0

for ind in xrange(Nace):
    soma_quad += (aceleracao[ind] - atmedio ) ** 2 

erro_padrao = math.sqrt( soma_quad / (Nace-1) )

print "Aceleracao teorica: ", ateorico, erro_aceleracao
print "Aceleracao media e erro: ", atmedio, erro_padrao