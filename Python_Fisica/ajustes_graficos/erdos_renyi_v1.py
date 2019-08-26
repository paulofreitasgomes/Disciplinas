#codigo em python 3

#pacote para fazer graficos
import matplotlib.pyplot as plt
#pacote para caracterizacao de redes
from networkx import nx

M = 100  # numero de vertices
p = 0.01 # probabilidade de conexao em um par aleatorio

#geracao da rede de Erdos Renyi, tambem chamada de binomial
grafo = nx.binomial_graph(M, p)

#escreve na tela informacoes gerais do grafo
print(nx.info(grafo))

#cria uma visualizacao do grafo
nx.draw(grafo,nodesize = 0.5)
#salva a visualizacao em um arquivo
plt.savefig('fig_erdos_renyi_v1a.png',dpi = 300, bbox_inches='tight') 

#calcula o numero de componentes
nc = nx.number_connected_components(grafo)
print(nc) #escreve na tela

#calcula o tamanho (numero de vertices) da maior componente
largest_cc = max(nx.connected_components(grafo), key=len)
sc = len(largest_cc)
print(sc) #escreve na tela