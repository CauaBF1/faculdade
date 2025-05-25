import random
import time


# Implementação do Countingsort_R (modificado para Radixsort) seguindo estritamente a apostila
def Countingsort_R(L, n, d):
    # Cria vetor S com mesmo tamanho de L para saída temporária
    S = [0] * n

    m = (L[0] // d) % 10  # Inicializa com o dígito d do primeiro elemento
    for i in range(1, n):
        current_digit = (L[i] // d) % 10
        if current_digit > m:
            m = current_digit

    C = [0] * (m + 1)  # Vetor de contagem para dígitos 0 a 9

    # Conta número de ocorrências de cada dígito 'd'
    # Loop 'for i = 0 to n – 1'
    for i in range(n):
        # Extrai o dígito 'd' do número L[i]
        # (L[i] // d) % 10 funciona para d=1, 10, 100, ...
        digito = (L[i] // d) % 10
        C[digito] += 1

    # Calcula a soma acumulada em C
    # Loop 'for i = 1 to m'
    for i in range(1, m + 1):
        C[i] += C[i - 1]

    # 2. Iteração direta conforme apostila
    for i in range(n):
        chave_atual = L[i]
        digito = (chave_atual // d) % 10
        C[digito] -= 1
        indice_s = C[digito]
        S[indice_s] = chave_atual

    # Copia o array ordenado S de volta para L
    # Loop 'for i = 0 to n – 1'
    for i in range(n):
        L[i] = S[i]


# Implementação do Radixsort seguindo estritamente a apostila
def Radixsort(L, n):
    # Encontra o maior elemento para saber o número de dígitos
    if n == 0:
        return
    m = L[0]
    for i in range(1, n):
        if L[i] > m:
            m = L[i]

    # Itera pelos dígitos, da unidade para o mais significativo
    d = 1  # Começa com o dígito das unidades (10^0)
    # Loop 'while m/d > 0'
    while m // d > 0:
        # Chama Countingsort_R para ordenar pelo dígito atual 'd'
        Countingsort_R(L, n, d)
        # Passa para o próximo dígito (dezenas, centenas, ...)
        d *= 10


# --- Execução e Teste ---

# Geração do array de 30 mil chaves aleatórias entre 1000 e 999999
n_q2 = 30000
min_val_q2 = 1000
max_val_q2 = 999999
L_q2 = [random.randint(min_val_q2, max_val_q2) for _ in range(n_q2)]


# Testar o algoritmo Radixsort e medir o tempo
inicio_q2 = time.time()
Radixsort(L_q2, n_q2)  # Radixsort ordena in-place
fim_q2 = time.time()

tempo_gasto_q2 = fim_q2 - inicio_q2


# Imprimir o tempo gasto
print(f"\nQuestão 2: Implementação do Radixsort conforme a apostila.")
print(f"Array de {n_q2} chaves aleatórias entre {min_val_q2} e {max_val_q2} gerado.")
print(f"Tempo gasto pelo Radixsort: {tempo_gasto_q2:.6f} segundos")
