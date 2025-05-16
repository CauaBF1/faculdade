'''
Autor: Cauã Borges Faria(834437)
Data de criação: 14/08/2024
Data de modificação: 14/08/2024
Objetivo:Maior valor da matriz.

'''
# Recebendo numero de linhas e colunas da matriz
nLinhas = int(input("Digite o numero de linhas da matriz: "))
nColunas = int(input("Digite o numero de colunas da matriz:"))

# Declarando matriz
matriz = []

# Entrada de dados da matriz
for i in range(nLinhas):
    linha = []
    for j in range(nColunas):
        valor = float(input(f"Digite o valor [{i}] [{j}] da matriz: "))
        linha.append(valor)
    matriz.append(linha)

# Calculo maior valor dentro da matriz
vmaior = 0
for i in range(nLinhas):
    for j in range(nColunas):
        if matriz[i][j] > vmaior:
            vmaior = matriz[i][j]

# Exibição da matriz e seu maior valor
print("Matriz: ")
for linha in matriz:
    print(linha)

print(f"O maior valor é: {vmaior}") 
