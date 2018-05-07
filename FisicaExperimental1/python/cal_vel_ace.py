tempo,posicao = np.loadtxt('posicao1.txt',usecols=[0,1],unpack=True);

nelementos = len(posicao); Deltat = tempo[1] - tempo[0];

velocidade = np.empty(nelementos-1,float);
aceleracao = np.empty(nelementos-1,float);

for i in range(nelementos-1): #calculo da velocidade
	velocidade[i] = (posicao[i+1] - posicao[i])/Deltat;

for i in range(1,nelementos-1): #calculo da aceleracao
	aceleracao[i] = (velocidade[i] - velocidade[i-1])/Deltat;
