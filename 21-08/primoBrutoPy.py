'''
Autor: Cauã Borges Faria(834437)
Data de criação: 21/08/2024
Data madificação: 21/08/2024
Objetivo: Mostre se numero é primo força bruta

'''
# Recebendo numero
print("Digite o numero:")
n = int(input());
primo = True

# Verificando se numero é primo
if n < 2:
    primo = False
    
for i in range(2, n):
    if(n % i == 0):
        primo = False

# Exibindo resultado
if primo:
    print(f"{num} é um numero primo")
else:
    print(f"{n} não é um numero primo")

