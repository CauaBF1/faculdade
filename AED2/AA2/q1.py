import random
import time


def Countingsort(L, n):
    # Passo 1: Encontrar o maior elemento da lista L.
    # O pseudocódigo da apostila usa m = max(L). Implementei iterativamente.
    if n == 0:
        return []
    m = L[0]  # Assume que L não está vazia
    for i in range(1, n):
        if L[i] > m:
            m = L[i]

    # Passo 2: Criar um vetor C de tamanho (m + 1) composto por zeros.
    # Índices de C irão de 0 a m.
    C = [0] * (m + 1)

    # Passo 3: Armazenar o número de ocorrências de cada elemento em C.
    # Loop 'for i = 0 to n - 1'
    for i in range(n):
        # L[i] é a chave (1 a m), usada como índice em C.
        C[L[i]] = C[L[i]] + 1

    # Passo 4: Calcular a soma cumulativa dos elementos de C.
    # Loop 'for i = 1 to m'
    for i in range(1, m + 1):
        C[i] = C[i] + C[i - 1]

    # Passo 5 & 6: Montar o array de saída S.
    # O pseudocódigo da apostila mostra 'for i = 0 to n - 1'.
    S = [0] * n  # Criar vetor S com mesmo tamanho de L
    for i in range(n):  # Iterando de 0 a n-1 conforme pseudocódigo
        chave_atual = L[i]
        # A posição em S é determinada pela contagem cumulativa C[chave_atual].
        # Decrementamos C[chave_atual] *antes* de usá-lo como índice (índice base 0).
        C[chave_atual] = C[chave_atual] - 1
        indice_s = C[chave_atual]
        # Coloca o elemento L[i] na sua posição ordenada em S.
        S[indice_s] = chave_atual

    # Retorna a lista ordenada S
    return S


# --- Execução e Teste ---

# Geração do array de 30 mil chaves aleatórias distintas entre 1 e 30000
n_q1 = 30000
# Gerar uma lista de 1 a 30000
lista_original_q1 = list(range(1, n_q1 + 1))
# Embaralhar a lista para obter chaves aleatórias distintas
L_q1 = lista_original_q1[:]  # Copiar a lista
random.shuffle(L_q1)


# Testar o algoritmo Countingsort e medir o tempo
inicio_q1 = time.time()
S_q1 = Countingsort(L_q1, n_q1)
fim_q1 = time.time()

tempo_gasto_q1 = fim_q1 - inicio_q1

# Imprimir o tempo gasto
print("Questão 1: Implementação do Countingsort conforme a apostila.")
print(f"Array de {n_q1} chaves aleatórias distintas entre 1 e {n_q1} gerado.")
print(f"Tempo gasto pelo Countingsort: {tempo_gasto_q1:.6f} segundos")
