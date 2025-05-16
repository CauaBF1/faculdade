'''
Autor: Cauã Borges Faria(834437)
Data de criação: 14/08/2024
Data de modificação: 14/08/2024
Objetivo: Encontrar elemento na matriz
'''

# Receber numero de linhas e colunas da matriz
nLinhas = int(input("Digite o numero de linhas da matriz: "))
nColunas = int(input("Digite o numero de colunas da matriz: "))

# Declarar a matriz
matriz = []

# Entrada de dados da matriz
for i in range(nLinhas):
    linha = []
    for j in range(nColunas):
        elemento = int(input(f"Digite o elemento [{i+1}] [{j+1}] da matriz: "))
        linha.append(elemento)
    matriz.append(linha)

# Elemento que deve ser procurado
elemento_procurado = int(input("Digite o elemento que deve ser procurado: "))

# Ver se o elemento está presente na matriz
encontrado = False
for i in range(nLinhas):
    for j in range(nColunas):
        if matriz[i][j] == elemento_procurado:
            print(f"Elemento está presente na matriz, linha {i+1} coluna {j+1}")
            encontrado = True

# Caso o elemento não esteja na matriz
if not encontrado:
    print("Elemento não está presente na matriz")

