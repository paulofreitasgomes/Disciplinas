
#Este codigo grafica a posicao e calcula a velocidade e aceleracao
#em funcao da posicao e tempo

import numpy as np
import matplotlib.pyplot as plt
import pylab

#Importando os dados de posicao e tempo
tempo,posicao = np.loadtxt('posicao1.txt',usecols=[0,1],unpack=True);

nelementos = len(posicao); #= numero de elementos em x
Deltat = tempo[1] - tempo[0];

#criando vetores vazios
velocidade = np.empty(nelementos-1,float);
aceleracao = np.empty(nelementos-1,float);

#calculo da velocidade
for i in range(nelementos-1):
	velocidade[i] = (posicao[i+1] - posicao[i])/Deltat;

#calculo da aceleracao
for i in range(1,nelementos-1): #repare que a contagem comeca em i = 1
	aceleracao[i] = (velocidade[i] - velocidade[i-1])/Deltat;


#Graficos
plt.subplot(3,1,1)
plt.title('Calculos usando a derivada aproximada',fontsize=14)
plt.plot(tempo,posicao,'ob', ms = 5,label = 'posicao')
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
plt.plot(tempo[0:nelementos-1],velocidade,'ok', ms = 5, label = 'velocidade')
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
plt.plot(tempo[0:nelementos-1],aceleracao,'or', ms = 5, label = 'aceleracao')
plt.xlabel('Tempo $t$ (s)', {'color': 'k','fontsize': 18})
plt.grid(True)
plt.ylabel('$a$ (m/s$^2$)', {'color': 'k','fontsize': 16})
plt.xticks(color='k', size=16)
#plt.yticks((-200, 700, 1600), ('-200', '700', '1600'))
plt.legend(loc='lower right',fontsize=12)
plt.savefig('gtrilho2.pdf',dpi=200)
#plt.show()
plt.close()


