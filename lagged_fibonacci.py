'''ARTHUR DE SOUSA COSTA - 20100515'''

import pandas as pd
import timeit
import random
import math

# Algoritmo de geração de números pseudoaleatórios com Additive Lagged Fibonacci.
def lagged_fibonacci(seed, m, j, k, qtd_numeros):
	# Lista que contém os números gerados para a ordem de grandeza atual.
	numeros = []
	# Lista que contém o tempo gasto para a geração dos números em questão.
	tempo = []
	# Criação da semente (sequência de números).
	x = []
	for nb in seed:
		x.append(int(nb))

	# São gerados números pseudoaleatórios de acordo com o número de 'qtd_numeros'.
	for i in range(0, qtd_numeros):
		# Obtém-se o tempo inicial.
		start_time = timeit.default_timer()
		# Operação realizada (soma).
		numero = (x[j-1+i] + x[k-1+i]) % m
		# Adiciona-se o número gerado na lista.
		numeros.append(numero)
		# Adiciona-se o número gerado na sequência de números.
		x.append(numero)
		# Obtém-se o tempo final.
		end_time = timeit.default_timer()

		# Cálculo do tempo gasto.
		total_time = end_time - start_time
		tempo.append(total_time * 10**6)

	return numeros, tempo


def get_lagged_fibonacci():
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
		# Quantidade de dígitos que um número da respectiva ordem de grandeza possui em média.
		digits = int(ord_grand[i] * math.log10(2))
		# Estratégia adotada: a seed é uma sequência de 10 números gerados pela biblioteca random do Python.
		# Cada número da sequência possui a quantidade de dígitos que um número daquela respectiva ordem de grandeza possui.
		# Por exemplo, um número de 40 bits (2^40) possui cerca de 12 dígitos decimais, pois 2^40 = 10^n ---> n = 12.
		seed = [random.randint(10**(digits-1), (10**digits)-1) for random_number in range(10)]
		# Módulo 'm', igual à ordem de grandeza. Deste modo, o número gerado estará nesta ordem.
		m = 2**ord_grand[i]
		# Posição do primeiro termo na sequência.
		j = 3
		# Posição do segundo termo na sequência.
		k = 7
		# Semente inicial. Vale ressaltar que o tamanho da sequência deve ser maior que 'k'. Mais explicações estão contidas no relatório.
		seed = seed
		if len(seed) < k:
			print(f"O tamanho da sequência inicial deve ser maior ou igual a 'k'. Tamanho da sequência: {len(seed)}. k: {k}.")
			return
		# São gerados 50 números por ordem de grandeza.
		qtd_numeros = 50
		# Algoritmo Additive Lagged Fibonacci.
		numeros, tempo = lagged_fibonacci(seed, m, j, k, qtd_numeros)

		numeros_list += numeros
		tamanho_list += [f'{ord_grand[i]} bits'] * len(numeros)
		tempo_list += tempo

	# Criação da tabela contendo informações sobre as operações feitas.
	df = pd.DataFrame()
	df['Algoritmo'] = ['Additive Lagged Fibonacci'] * len(numeros_list)
	df['Tamanho do número'] = tamanho_list
	df['Número gerado'] = numeros_list
	df['Tempo para gerar em µs'] = tempo_list
	df.to_csv('lagged_fibonacci.csv', index=False)

if __name__ == "__main__":
	get_lagged_fibonacci()