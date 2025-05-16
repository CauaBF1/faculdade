'''
Autor: Cauã Borges Faria(834437)
Data de criação: 21/08/2024
Data madificação: 21/08/2024
Objetivo: Calcule e mostre os dados do vinho mais caro (nome, preço e tipo).
'''

# Declara variavel do maior preço
precoMaior = 0
while 1:
    # Recebe o tipo de vinhp
    print("Digite o tipo do vinho (T = Tinto, B = Branco, R = Rosé ou FIM para parar): ");
    # Converte para maiúsculas
    tipo = input().strip().upper()
    if tipo == 'FIM':
        break
    # Recebe o nome do vinho
    print("Digite o nome do vinho: ")
    nome = input()
    # Recebe o valor do vinho
    print("Digite o valor do vinho: ")
    valor = float(input())
    # Validando vinho mais caro
    if(valor > precoMaior):
        tipoCaro = tipo
        nomeCaro = nome
        precoMaior = valor
    
# Modificando variavel tipo para escrever tipo do vinho
if(tipoCaro == 'T'):
    tipoCaro = 'Tinto'
if(tipoCaro == 'B'):
    tipoCaro = 'Branco'
if(tipoCaro == 'R'):
    tipoCaro = 'Rosé'
    
# Exibindo resultado
print(f"O tipo do vinho mais caro é: {tipoCaro}")
print(f"O nome do vinho mais caro é: {nomeCaro}")
print(f"O preço do vinho mais caro é: R${precoMaior:.2f}")
