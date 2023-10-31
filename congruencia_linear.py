'''ARTHUR DE SOUSA COSTA - 20100515'''

import pandas as pd
import timeit
from datetime import datetime
import math

# Algoritmo de geração de números pseudoaleatórios com Congruência Linear.
def congruencia_linear(seed, m, a, c, qtd_numeros):
	# Lista que contém os números gerados para a ordem de grandeza atual.
	numeros = []
	# Lista que contém o tempo gasto para a geração dos números em questão.
	tempo = []
	# Semente inicial.
	x = seed

	# São gerados números pseudoaleatórios de acordo com o número de 'qtd_numeros'.
	for i in range(0, qtd_numeros):
		# Obtém-se o tempo inicial.
		start_time = timeit.default_timer()
		# Operação realizada.
		numero = ((x * a) + c) % m
		# Adiciona-se o número gerado na lista.
		numeros.append(numero)
		# Próxima semente.
		x = numero
		# Obtém-se o tempo final.
		end_time = timeit.default_timer()

		# Cálculo do tempo gasto.
		total_time = end_time - start_time
		tempo.append(total_time * 10**6)
		
	return numeros, tempo


def get_congruencia_linear():
	# Lista que contém todos os números gerados.
	numeros_list = []
	# Lista que contém o tamanho de todos os números gerados.
	tamanho_list = []
	# Lista que contém o tempo gasto para a geração de todos os números.
	tempo_list = []
	# Ordens de grandeza dos números (em bits).
	ord_grand = [40, 56, 80, 128, 168, 224, 256, 512, 1024, 2048, 4096]

	# Para cada ordem de grandeza, são gerados números pseudoaleatórios.
	for i in range(0, len(ord_grand)):
		# A seed é o número inteiro do timestamp atual.
		seed = int(datetime.now().timestamp())
		# Quantidade de dígitos que um número da respectiva ordem de grandeza possui em média.
		digits = int(ord_grand[i] * math.log10(2))
		# Estratégia adotada: concatenar a seed suscetivamente até possuir no mínimo a quantidade de dígitos
		# que um número daquela respectiva ordem de grandeza possui. Por exemplo, um número de 40 bits (2^40)
		# possui cerca de 12 dígitos decimais, pois 2^40 = 10^n ---> n = 12.
		seed = str(seed)
		while len(seed) < digits:
			seed += seed
		seed = int(seed)
		# Módulo 'm', igual à ordem de grandeza. Deste modo, o número gerado estará nesta ordem.
		m = 2**ord_grand[i]
		# Multiplicador 'a'.
		a = 3
		# Incremento 'c'.
		c = 7
		# São gerados 50 números por ordem de grandeza.
		qtd_numeros = 50
		# Algoritmo de Congruência Linear.
		numeros, tempo = congruencia_linear(seed, m, a, c, qtd_numeros)

		numeros_list += numeros
		tamanho_list += [f'{ord_grand[i]} bits'] * len(numeros)
		tempo_list += tempo

	# Criação da tabela contendo informações sobre as operações feitas.
	df = pd.DataFrame()
	df['Algoritmo'] = ['Congruência Linear'] * len(numeros_list)
	df['Tamanho do número'] = tamanho_list
	df['Número gerado'] = numeros_list
	df['Tempo para gerar em µs'] = tempo_list
	df.to_csv('congruencia_linear.csv', index=False)

if __name__ == "__main__":
	get_congruencia_linear()