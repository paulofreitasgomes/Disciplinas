import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

Q, Nt = 80, 4 
tempo = np.linspace(0,Nt,Q)
Ms, Lmax = 20, 2

def forca(state, tempo): #Expressao da forca gravitacional
	x, y, vx, vy = state
	return vx, vy, -Ms*x/(x**2+y**2)**(3.0/2.0), -Ms*y/(x**2+y**2)**(3.0/2.0)

pos0, post = [], []
v0 = np.linspace(0.50, 3.16, 6)
Nv0 = len(v0)

for i2 in range(Nv0):
	pos0.append([2.0, 0.0, 0.0, v0[i2]]) #Condicao inicial x0,y0,vx0,vy0
	post.append(odeint(forca, pos0[i2], tempo)) #Runge Kutta

for t2 in range(Q): # Graficos
	plt.scatter(0,0, s=250, marker= 'o',color='k') #sol parado na origem
	for i1 in range(Nv0):
		plt.plot(post[i1][:,0][1:t2+1], post[i1][:,1][1:t2+1], lw = 1.5) #trajetoria
		plt.scatter(post[i1][:,0][t2],post[i1][:,1][t2], s=100, marker= 'o') #posicao
	plt.axis('scaled')
	plt.title('$t=$'+str(t2),fontsize = 18)
	plt.xlabel('x')
	plt.ylabel('y')
	axes = plt.gca()
	axes.set_xlim([-Lmax,Lmax])
	axes.set_ylim([-Lmax,Lmax])
	plt.savefig('figura'+str(t2)+'.png')
	plt.close()
