'''ARTHUR DE SOUSA COSTA - 20100515'''

import random

# Teste de primalidade utilizando o pequeno Teorema de Fermat.
# Se 'n' é primo, sempre retornará True. Se 'n' é composto, pode retornar False com alta probabilidade.
# A probabilidade de sucesso aumenta à medida que aumenta-se o número de 'steps'.
def get_fermat(n, steps):

    # Se 'n' é igual a 2 ou 3, automaticamente é um número primo. Essa verificação é feita para evitar erros na atribuição de 'a' (1 < a < n-1).
    if (n == 2) or (n == 3):
        return True

    # Se n é menor ou igual a 1 ou par (com exceção do 2), automaticamente não é um número primo.
    if (n <= 1) or (n % 2 == 0):
        return False

    # Verifica se 'n' é primo com base no Teorema (a^n-1 ≡ 1(mod n)). O número de tentativas é igual ao número de 'steps'.
    for i in range(steps):
        a = random.randrange(2, n - 1)
        if pow(a, n - 1, n) != 1:
            return False
    return True


if __name__ == "__main__":
    # Exemplo contendo um número pseudoprimo e com apenas 1 'step'. O teste falha algumas vezes. Mais informações estão contidas no relatório.
    n = 2047
    steps = 1
    print(get_fermat(n, steps))