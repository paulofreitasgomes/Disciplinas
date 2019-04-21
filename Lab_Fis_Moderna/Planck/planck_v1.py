#Importacao de modulos a serem usados
import numpy as np #uso de vetores
import matplotlib.pyplot as plt #graficos
from scipy.optimize import curve_fit #ajuste linear

###### Funcoes ################
    
def grafico1(vx,vy,nome):
    plt.plot(vx,vy,'ob')
    plt.xlabel(r'$V$',fontsize = 16)
    plt.ylabel(r'$I$',fontsize = 16)
    titulo = r'Determinacao da constante de Planck'
    plt.title(titulo,fontsize=16)   
#Salva a figura em um arquivo
    plt.savefig(nome,dpi = 300, bbox_inches='tight')
    plt.close()

def grafico2(vx,dados,ajuste,nome):
    plt.plot(vx,dados,'ob', ms = 6, label = 'Dados')
    plt.plot(vx,ajuste,'-r', lw = 2, label = 'Ajuste')
    plt.xlabel(r'$V$',fontsize = 16)
    plt.ylabel(r'$I$',fontsize = 16)
    plt.title('Curva IV: LED',fontsize=16)
    plt.legend(loc='lower left',fontsize = 14)
    plt.xticks(size=16) #define o tamanho da fonte nos
    plt.yticks(size=16) # eixos em 16
    plt.savefig(nome,dpi = 300, bbox_inches='tight')
    plt.close()

#funcao que define a reta
def reta(x,a,b, dtype = float):
    return a + b*x
    
#funcao que faz o ajuste e guarda os parametros e erros
def faz_ajuste(f1,vetorx,vetory,c2):
    parametros, erros5 = curve_fit(f1, vetorx, vetory,c2)
    lista_erros = []
    lista_erros.append(np.sqrt(erros5[0,0])) #erro em a
    lista_erros.append(np.sqrt(erros5[1,1])) #erro em b
    return parametros, lista_erros

################################
#Inicio do programa

#amostra de dados para teste
#tensao
vx = [1.99,1.98,1.97,1.96,1.95,1.94,1.93,1.92,1.90]
#corrente
vy = [12.6,12.4,11.2,10.7,10.1,9.2,8.2,7.4,6.4]

#gera o grafico 1
grafico1(vx,vy,'fig1.png')

#Fazendo ajuste
chute = [1.9,6] #valores iniciais
para, erros = faz_ajuste(reta,vx,vy,chute)

#calculo da funcao ajustada usando os parametros encontrados
nx = len(vx) #numero de elementos na lista vx
vy2 = np.zeros(nx) #criando um vetor de zeros com nx componentes
for i1 in range(nx):
    vy2[i1] = para[0] + para[1]*vx[i1]

#gerando o grafico 2
grafico2(vx,vy,vy2,'fig3.png')