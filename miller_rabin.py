'''ARTHUR DE SOUSA COSTA - 20100515'''

import random

# Teste de primalidade utilizando o Algoritmo de Miller-Rabin.
def miller_rabin(n):

    # Se n é igual a 2 ou 3, automaticamente é um número primo. Essa verificação é feita para evitar erros na atribuição de 'a' (1 < a < n-1).
    if (n == 2) or (n == 3):
        return True

    # Se n é menor ou igual a 1 ou par (com exceção do 2), automaticamente não é um número primo.
    if (n <= 1) or (n % 2 == 0):
        return False

    # Escrevemos que (n - 1 = 2^k * m), onde k > 0 e 'm' é a parte ímpar do número.
    # Deste modo, abaixo encontramos os valores de 'k' e 'm'.
    k = 0
    m = n - 1
    while m % 2 == 0:
        k += 1
        m //= 2

    # Atribuímos um valor para 'a' e calculamos 'b' (b = a^m mod n).
    a = random.randrange(2, n - 1)
    b = pow(a, m, n)

    # Se b ≡ 1 (mod n), então 'n' é provavelmente primo.
    if (b == 1) or (b == n - 1):
        return True
    
    # Para i = 0 ate k - 1, calculamos 'b' (b = b^2 mod n).
    # Se b ≡ - 1 (mod n) , então 'n' é provavelmente primo.
    for j in range(0, k):
        b = pow(b, 2, n)
        if b == n - 1:
            return True
    
    # Se nenhuma das condições acima forem satisfeitas, então 'n' é com certeza composto.
    return False

# Função que retorna se 'n' é primo ou composto.
# Se 'n' for composto, sempre retornará False (pois nenhuma das condições foi satisfeita).
# Se 'n' é primo, pode retornar True, mas não é necessariamente primo.
# A probabilidade de sucesso aumenta à medida que aumenta-se o número de 'steps'.
def get_miller_rabin(n, steps):
    for i in range(steps):
        if miller_rabin(n) == False:
            return False
    return True


if __name__ == "__main__":
    # Exemplo contendo um número pseudoprimo e com apenas 1 'step'. O teste falha algumas vezes. Mais informações estão contidas no relatório.
    n = 2047
    steps = 1
    print(get_miller_rabin(n, steps))