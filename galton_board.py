import matplotlib.pyplot as plt
import random

pelotas = 40
niveles = 6


class TableroGalton():
	def __init__(self,pelotas,niveles):
		self.pelotas = pelotas
		self.niveles = niveles

	def crear_experimento(self) -> list:
		dist = [0] * ((self.niveles * 2) + 1)
		for ball in range(0, self.pelotas):
			total = 0
			for line in range(1, self.niveles+1):	
				resultado = random.uniform(0, 1)
				if(resultado >= 0.5):
					total += 1
				else:
					total -= 1	
			dist[total + self.niveles] += 1 

		for i in range(0, self.niveles + 1):
			dist[i] = dist[i*2]	
		return dist[0:self.niveles+1]

	def graficar_resultados_experimento(self,datos):
		plt.bar([str(i) for i in range(0, self.niveles + 1)], datos[0:self.niveles+1])
		plt.xticks([])
		plt.show()

tablero = TableroGalton(pelotas, niveles)
experimento = tablero.crear_experimento()
tablero.graficar_resultados_experimento(experimento)
