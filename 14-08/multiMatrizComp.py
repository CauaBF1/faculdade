'''
Autor: Cauã Borges Faria(834437)
Data de criação: 14/08/2024
Data de modificação: 14/08/2024
Objetivo:Multiplicação de matrizes
'''

# Entrada do número de linhas e de colunas das matrizes
nLinhas = int(input("Digite o numero de linhas da matriz 1: "))
nColunas1 = int(input("Digite o numero de colunas da matriz 1/linhas da matriz 2: "))
nColunas2 = int(input("Digite o numero de colunas da matriz 2: "))
# Declaração das matrizes
matriz1 = []
matriz2 = []
resultado =[]

# Entrada de dados da matriz1
for i in range(nLinhas):
    linha = []
    for j in range(nColunas1):
        valor = float(input(f"Digite o elemento [{i}][{j}] da matriz1: "))
        linha.append(valor)
    matriz1.append(linha)

# Entrada de dados da matriz2
for i in range(nColunas1):
    linha = []
    for j in range(nColunas2):
        valor = float(input(f"Digite o elemento [{i}][{j}] da matriz2: "))
        linha.append(valor)
    matriz2.append(linha)

# Mostrando as matrizes
print("Matriz 1:")
for linha in matriz1:
    print(linha)

print("Matriz 2:")
for linha in matriz2:
    print(linha)


# multiplicação de matrizes
for i in range(nLinhas):
    linha_resultado = []
    for j in range(nColunas2):
        resultado_elemento = 0  
        for k in range(nColunas1):
            resultado_elemento += matriz1[i][k] * matriz2[k][j]
        linha_resultado.append(resultado_elemento)  
    resultado.append(linha_resultado) 

# Exbindo resultado
print("Resultado: ")
for linha in resultado:
    print(linha)




