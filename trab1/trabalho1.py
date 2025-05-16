import time
import random
import copy

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def comb_sort(arr):
    gap = len(arr)
    shrink = 1.3
    sorted = False

    while not sorted:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sorted = True

        for i in range(len(arr) - gap):
            if arr[i] > arr[i + gap]:
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False

def exec_time(func, arr):
    start_time = time.time()
    func(arr)
    end_time = time.time()
    return end_time - start_time

def gerar_numeros(qtd_numeros):
    return [random.randint(0, 1000) for _ in range(qtd_numeros)]

# de 2000 ate < 50001 indo de 2000 em 2000
for tamanho in range(2000, 50001, 2000):
    vetor_original = gerar_numeros(tamanho)

    # Bubble Sort
    vetor_bubble = copy.deepcopy(vetor_original)
    tempo_bubble = exec_time(bubble_sort, vetor_bubble)
    print(f"Bubble Sort - Tamanho {tamanho}: {tempo_bubble:.4f} segundos")

    # Selection Sort
    vetor_selection = copy.deepcopy(vetor_original)
    tempo_selection = exec_time(selection_sort, vetor_selection)
    print(f"Selection Sort - Tamanho {tamanho}: {tempo_selection:.4f} segundos")

    # Insertion Sort
    vetor_insertion = copy.deepcopy(vetor_original)
    tempo_insertion = exec_time(insertion_sort, vetor_insertion)
    print(f"Insertion Sort - Tamanho {tamanho}: {tempo_insertion:.4f} segundos")

    # Comb Sort
    vetor_comb = copy.deepcopy(vetor_original)
    tempo_comb = exec_time(comb_sort, vetor_comb)
    print(f"Comb Sort - Tamanho {tamanho}: {tempo_comb:.4f} segundos")

    print("-" * 50)  # Separador para cada teste

