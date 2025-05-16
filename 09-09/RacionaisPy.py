'''
Autor: Cauã Borges Faria
Data de criação: 09/07/24
Data de modificação: 09/07/24
Objetivo: Ler dois números racionais, simplificá-los, somá-los e multiplicá-los.
'''

from math import gcd

class tRacional:
    """
    Sub-rotina: __init__
    Objetivo: Inicializar um número racional e simplificá-lo.
    Parâmetros:
    - n: Numerador (entrada de dados)
    - d: Denominador (entrada de dados)
    Valor de Retorno:
    - Nenhum
    """
    def __init__(self, n, d):
        if d == 0:
            raise ValueError("O denominador não pode ser zero.")
        self.n = n
        self.d = d
        self.simplificar()

    """
    Sub-rotina: simplificar
    Objetivo: Simplificar o número racional utilizando o MDC.
    Parâmetros:
    - Nenhum
    Valor de Retorno:
    - Nenhum
    """
    def simplificar(self):
        divisor_comum = gcd(self.n, self.d)
        self.n //= divisor_comum
        self.d //= divisor_comum
        if self.d < 0:  # Para garantir que o denominador seja positivo
            self.n = -self.n
            self.d = -self.d

    """
    Sub-rotina: __str__
    Objetivo: Retornar uma string que representa o número racional na forma "n/d".
    Parâmetros:
    - Nenhum
    Valor de Retorno:
    - String representando o número racional
    """
    def __str__(self):
        return f"{self.n}/{self.d}"

"""
Sub-rotina: ler_racional
Objetivo: Ler os valores de numerador e denominador do usuário e criar um número racional simplificado.
Parâmetros:
- Nenhum
Valor de Retorno:
- Objeto tRacional simplificado
"""
def ler_racional():
    n = int(input("Digite o numerador: "))
    d = int(input("Digite o denominador: "))
    return tRacional(n, d)

"""
Sub-rotina: escrever_racional
Objetivo: Exibir o número racional na tela.
Parâmetros:
- r: Número racional (entrada de dados)
Valor de Retorno:
- Nenhum
"""
def escrever_racional(r):
    print(f"O número racional é: {r}")

"""
Sub-rotina: somar_racionais
Objetivo: Somar dois números racionais e retornar o resultado simplificado.
Parâmetros:
- r1: Primeiro número racional (entrada de dados)
- r2: Segundo número racional (entrada de dados)
Valor de Retorno:
- Objeto tRacional representando a soma simplificada
"""
def somar_racionais(r1, r2):
    numerador = r1.n * r2.d + r2.n * r1.d
    denominador = r1.d * r2.d
    return tRacional(numerador, denominador)

"""
Sub-rotina: multiplicar_racionais
Objetivo: Multiplicar dois números racionais e retornar o resultado simplificado.
Parâmetros:
- r1: Primeiro número racional (entrada de dados)
- r2: Segundo número racional (entrada de dados)
Valor de Retorno:
- Objeto tRacional representando o produto simplificado
"""
def multiplicar_racionais(r1, r2):
    numerador = r1.n * r2.n
    denominador = r1.d * r2.d
    return tRacional(numerador, denominador)


# Leitura de dois números racionais
r1 = ler_racional()
r2 = ler_racional()

# Escrever os números racionais
escrever_racional(r1)
escrever_racional(r2)

# Somar os dois números racionais
soma = somar_racionais(r1, r2)
print("Resultado da soma:", soma)


# Multiplicar os dois números racionais
produto = multiplicar_racionais(r1, r2)
print("Resultado da multiplicação:", produto)

