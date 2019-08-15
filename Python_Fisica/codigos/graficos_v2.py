import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#funcao para criar o grafico
#repare na identacao
def cria_grafico(nome,d0):
    plt.plot(d0.d,d0.S,'-ob',lw = 0.5) #primeira sequencia de dados
    plt.plot(d0.d,d0.mC,'--sr',lw = 0.5) #segunda sequencia de dados
    plt.xlabel('delta',fontsize = 16) #nome do titulo no eixo x
    plt.ylabel('S',fontsize = 16) #nome do titulo no eixo y
    titulo = 'Meu segundo grafico.' #define o titulo
    plt.title(titulo,fontsize=16) #insere o titulo
    plt.grid(True) #cria um grid regular 
    plt.legend(loc='upper right',fontsize = 14) #insere a legenda
    plt.xticks(size=14) #tamanho da fonte dos valores no eixo x
    plt.yticks(size=14) #tamanho da fonte dos valores no eixo y
    axes = plt.gca()
    axes.set_xlim([0.0,8]) #define o intervalo no eixo x
    axes.set_ylim([0.0,1.0]) #define o intervalo no eixo y
    plt.savefig(nome,dpi = 300, bbox_inches='tight') #salva o grafico em um arquivo
    plt.close() #fecha a figura, recomendado.


################################################################
################################################################

#importando os dados como um dataframe (funcao do pacote pandas)
dados = pd.read_csv('dados_v2.txt', header = 0, sep = '|')

#executa a funcao que gera o grafico
cria_grafico('figura_v2.png',dados)
