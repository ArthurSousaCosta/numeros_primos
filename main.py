'''ARTHUR DE SOUSA COSTA - 20100515'''

from congruencia_linear import *
from lagged_fibonacci import *
from miller_rabin import *
from fermat import *

# Função que cria tabela dos numeros pseudoaleatórios automaticamente.
def criar_tabela_pt1():
    df_cl = pd.read_csv('congruencia_linear.csv')
    tamanho_list = []
    media_tempo_list = []
    for ord_gran in df_cl['Tamanho do número'].unique():
        media_tempo = df_cl.loc[df_cl['Tamanho do número'] == ord_gran, 'Tempo para gerar em µs'].mean()
        tamanho_list.append(ord_gran)
        media_tempo_list.append(media_tempo)
    df_cl = pd.DataFrame()
    df_cl['Algoritmo'] = ['Congruência Linear'] * len(tamanho_list)
    df_cl['Tamanho do número'] = tamanho_list
    df_cl['Tempo médio para gerar em µs'] = media_tempo_list

    df_lf = pd.read_csv('lagged_fibonacci.csv')
    tamanho_list = []
    media_tempo_list = []
    for ord_gran in df_lf['Tamanho do número'].unique():
        media_tempo = df_lf.loc[df_lf['Tamanho do número'] == ord_gran, 'Tempo para gerar em µs'].mean()
        tamanho_list.append(ord_gran)
        media_tempo_list.append(media_tempo)
    df_lf = pd.DataFrame()
    df_lf['Algoritmo'] = ['Additive Lagged Fibonacci'] * len(tamanho_list)
    df_lf['Tamanho do número'] = tamanho_list
    df_lf['Tempo médio para gerar em µs'] = media_tempo_list

    df_final = pd.concat([df_cl, df_lf])
    df_final.to_csv('numeros_pseudoaleatorios.csv', index=False)


if __name__ == "__main__":
    '''CONGRUÊNCIA LINEAR'''
    # Algoritmo de geração de números pseudoaleatórios com Congruência Linear.
    get_congruencia_linear()

    '''ADDITIVE LAGGED FIBONACCI'''
    # Algoritmo de geração de números pseudoaleatórios com Additive Lagged Fibonacci.
    get_lagged_fibonacci()

    '''TABELA PARTE 1'''
    # Criar tabela dos números pseudoaleatórios gerados.
    criar_tabela_pt1()

    '''LISTAS PARA TABELA PARTE 2'''
    # Lista com os nomes dos métodos de teste de primalidade.
    metodos_list = []
    # Lista com o tamanho dos números usados no teste.
    tamanho_list = []
    # Lista com os números primos testados.
    numeros_list = []
    # Lista com os tempos gastos para testar os números.
    tempo_list = []

    ''''LEITURA DOS NÚMEROS GERADOS NA PARTE 1'''
    # Ler os números gerados, apenas 1 de cada ordem de grandeza. Caso não seja primo, este será incrementado
    # e o teste será feito novamente, a fim de pegar pelo menos um número primo de cada ordem de grandeza.
    df_cl = pd.read_csv('congruencia_linear.csv')
    df_lf = pd.read_csv('lagged_fibonacci.csv')
    ordens = ['40 bits', '56 bits', '80 bits', '128 bits', '168 bits', '224 bits', '256 bits', '512 bits', '1024 bits', '2048 bits', '4096 bits']
    tamanhos = []
    numeros = []
    for o in ordens:
        tamanhos.append(df_cl.loc[df_cl['Tamanho do número'] == o].iloc[0]['Tamanho do número'])
        numeros.append(df_cl.loc[df_cl['Tamanho do número'] == o].iloc[0]['Número gerado'])
    for o in ordens:
        tamanhos.append(df_lf.loc[df_lf['Tamanho do número'] == o].iloc[0]['Tamanho do número'])
        numeros.append(df_lf.loc[df_lf['Tamanho do número'] == o].iloc[0]['Número gerado'])

    '''MILLER-RABIN'''
    # Fazer o teste de primalidade com o Algoritmo de Miller-Rabin
    # Utilizando 3 passos.
    steps = 3
    # Realizar o teste para cada número.
    for i in range(len(numeros)):
        n = int(numeros[i])
        while True:
            # Obtém-se o tempo inicial.
            start_time = timeit.default_timer()
            # Resultado do teste.
            result = get_miller_rabin(n, steps)
            # Obtém-se o tempo final.
            end_time = timeit.default_timer()
            # Cálculo do tempo gasto.
            total_time = end_time - start_time
            # Se for primo, adiciona na tabela.
            if result == True:
                metodos_list.append('Miller-Rabin')
                tamanho_list.append(tamanhos[i])
                numeros_list.append(n)
                tempo_list.append(total_time * 10**6)
                break
            # Caso não seja primo, incrementa-se 1 a fim de encontrar pelo menos um número daquela ordem de grandeza.
            else:
                n += 1

    '''FERMAT'''
    # Fazer o teste de primalidade com o Teorema de Fermat.
    # Utilizando 3 passos.
    steps = 3
    # Realizar o teste para cada número.
    for i in range(len(numeros)):
        n = int(numeros[i])
        while True:
            # Obtém-se o tempo inicial.
            start_time = timeit.default_timer()
            # Resultado do teste.
            result = get_fermat(n, steps)
            # Obtém-se o tempo final.
            end_time = timeit.default_timer()
            # Cálculo do tempo gasto.
            total_time = end_time - start_time
            # Se for primo, adiciona na tabela.
            if result == True:
                metodos_list.append('Fermat')
                tamanho_list.append(tamanhos[i])
                numeros_list.append(n)
                tempo_list.append(total_time * 10**6)
                break
            # Caso não seja primo, incrementa-se 1 a fim de encontrar pelo menos um número daquela ordem de grandeza.
            else:
                n += 1

    '''TABELA PARTE 2'''
	# Criação da tabela contendo informações sobre as operações feitas.
    df_pt2 = pd.DataFrame()
    df_pt2['Método'] = metodos_list
    df_pt2['Tamanho do número'] = tamanho_list
    df_pt2['Número primo gerado'] = numeros_list
    df_pt2['Tempo para testar em µs'] = tempo_list
    df_pt2.to_csv('verificacao_primalidade.csv', index=False)