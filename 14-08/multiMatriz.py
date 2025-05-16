'''
Autor: Cauã Borges Faria(834437)
Data de criação: 14/08/2024
Data de modificação: 14/08/2024
Objetivo:multiplicação da linha i da matriz A com a coluna j da matriz B, ambas de ordem n x n (quadrática).
Deve-se ler a ordem das matrizes, os elementos de cada matriz, realizar a multiplicação e por fim apresentar o resultado da multiplicação.
'''

# Entrada do número de linhas e de colunas das matrizes
nLinhas = int(input("Digite o numero de linhas das matrizes: "))
nColunas = int(input("Digite o numero de colunas das matrizes: "))

# Declaração das matrizes
matriz1 = []
matriz2 = []

# Entrada de dados da matriz1
for i in range(nLinhas):
    linha = []
    for j in range(nColunas):
        valor = float(input(f"Digite o elemento [{i}][{j}] da matriz1: "))
        linha.append(valor)
    matriz1.append(linha)

# Entrada de dados da matriz2
for i in range(nLinhas):
    linha = []
    for j in range(nColunas):
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
    
# Entrada de qual linha e coluna devem ser multiplicadas 
linhaMult = int(input('Digite a linha da matriz A que deseja multiplicar: '))
colunaMult = int(input('Digite a coluna da matriz B que deseja multiplicar: '))

# multiplicação da linha e da coluna, com validação se existe a linha e a coluna que vão ser multiplicadas
if linhaMult < 1 or linhaMult > nLinhas or colunaMult < 1 or colunaMult > nColunas:
    print("Linha ou coluna fora dos limites!")
else:
    res = 0
    for i in range(nLinhas):  
        res += matriz1[linhaMult-1][i] * matriz2[i][colunaMult-1]  

    print(f"O resultado é: {res}")



