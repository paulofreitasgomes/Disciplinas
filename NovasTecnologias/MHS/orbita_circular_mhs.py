import matplotlib.pyplot as plt
import math
import numpy as np

plt.rc('text', usetex=True)
plt.rc('font', family='serif')

lado = 10
raio = 8.0
omega = 1.0
N = 150 #numero de iteracoes
tempo = np.linspace(0,2*math.pi/omega,N)
origem = [0,0]

i=0
for t in tempo:
	circulo = plt.Circle((0,0), raio, edgecolor = 'b', facecolor = 'none')
	pos_circulo = (raio*math.cos(omega*t),raio*math.sin(omega*t))
	pos_eixo_x = (raio*math.cos(omega*t),0)
	trajetoria1 = plt.Circle(pos_circulo, 0.2, color = 'r')
	trajetoria2 = plt.Circle(pos_eixo_x, 0.2, color = 'r')
	# vetor_x = [0,pos_circulo[0]]
	# vetor_y = [0,pos_circulo[1]]
	# vetor_y0 = [0,0]
	fig = plt.gcf()
	#plt.plot(vetor_x,vetor_y,'-k', lw = 2)
	#plt.plot(vetor_x,vetor_y0,'-g', lw = 2)
	plt.xticks([])
	plt.yticks([])
	plt.axis('scaled')
	ax = fig.gca()
	ax.quiver(0.0, 0.0, pos_circulo[0], pos_circulo[1], color = 'k', angles='xy', scale_units = 'xy', scale = 1)
	ax.quiver(0.0, 0.0, pos_circulo[0], 0, color = 'g', angles='xy', scale_units = 'xy', scale = 1)
	projx, projy = [pos_circulo[0],pos_circulo[0]], [0,pos_circulo[1]]
	plt.plot(projx, projy, '--m', lw = 1)
	ax.add_artist(trajetoria1)
	ax.add_artist(trajetoria2)
	ax.add_artist(circulo)
	ax.set_xlim([-lado,lado])
	ax.set_ylim([-lado,lado])
	plt.title('Movimento circular e oscilador harmonico.')
	# plt.text(0.0,0.8,r'$+e$', color = 'b')
	# plt.text(5.5,0.8,r'$-e$', color = 'b')
	plt.text(-lado+1.0, lado - 2.0,r'$\theta=$ '+str(round(omega*t,2)))
	plt.text(lado-4.0, lado - 2.0,r'$t=$ '+str(round(t,2)))
	plt.text(lado-4.0, -lado + 2.0,r'$x=$ '+str(round(pos_circulo[0],2)), color = 'g')
	plt.text(-lado+1.0, -lado + 2.0,r'$r=$ '+str(raio))
	#print('Gravando figura:',i)
	plt.savefig('circulo_mhs_'+str(i)+'.png', dpi = 300, bbox_inches='tight')
	i += 1
	plt.close()
