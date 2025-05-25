import math
import random
import time


# Implementação do Bucketsort
def Bucketsort(L, n):
    # Passo 1: Criar n baldes vazios.
    # lista de listas em Python.
    # O pseudocódigo usa 'B' para os baldes.
    B = [[] for _ in range(n)]  # B[i] = NIL

    # Passo 2: Inserir elementos nos baldes apropriados.
    # Loop 'for i = 0 to n – 1'
    K = 200.0  # Limite superior do intervalo original [0.0, 200.0]

    for i in range(n):
        chave_atual = L[i]

        # O pseudocódigo da apostila trata o valor 1 (limite superior de [0,1)) separadamente.
        # Adaptar para o limite superior 200.0.
        if chave_atual >= K:  # Trata o caso L[i] == 200.0 (ou ligeiramente acima)
            index = n - 1
        elif (
            chave_atual < 0
        ):  # Trata valores negativos (msm a questão dizendo de 0 a 200)
            index = 0  # Coloca no primeiro balde
        else:
            # index = floor(n * L[i]) para [0,1)
            # Adaptado: index = floor(n * (chave_atual / K))
            # Evita divisão por zero se K for 0, mas K=200.0 aqui.
            normalized_value = chave_atual / K
            index = math.floor(n * normalized_value)

        # Garante que o índice esteja dentro dos limites [0, n-1]
        # Embora a lógica acima deva cuidar disso, uma verificação nunca é dms né.
        index = max(0, min(n - 1, index))

        # insert(B[index], L[i]) - Usamos append em Python
        B[index].append(chave_atual)

    # Passo 3: Ordenar cada balde individualmente.
    # Loop 'for i = 0 to n – 1'
    # O pseudocódigo usa 'sort(B[i])'. Usaremos sort() do Python (Insertion Sort é comum, mas sort() é eficiente).
    for i in range(n):
        B[i].sort()  # Ordena o balde B[i] in-place

    # Passo 4: Concatenar os baldes ordenados para formar a lista final S.
    # S = concatenate(B[0], B[1], …, B[n-1])
    S = []
    for i in range(n):
        S.extend(B[i])  # Adiciona todos os elementos do balde B[i] a S

    # Retorna a lista ordenada S
    return S


# --- Execução e Teste ---

# Geração do array de 30 mil chaves aleatórias float entre 0 e 200
n_q3 = 30000
min_val_q3 = 0.0
max_val_q3 = 200.0
# random.uniform(a, b) gera um float x tal que a <= x <= b
L_q3 = [random.uniform(min_val_q3, max_val_q3) for _ in range(n_q3)]


# Testar o algoritmo Bucketsort e medir o tempo
inicio_q3 = time.time()
S_q3 = Bucketsort(L_q3, n_q3)
fim_q3 = time.time()

tempo_gasto_q3 = fim_q3 - inicio_q3


# Imprimir o tempo gasto
print(f"\nQuestão 3: Implementação do Bucketsort conforme a apostila.")
print(
    f"Array de {n_q3} chaves aleatórias float entre {min_val_q3} e {max_val_q3} gerado."
)
print(f"Tempo gasto pelo Bucketsort: {tempo_gasto_q3:.6f} segundos")
