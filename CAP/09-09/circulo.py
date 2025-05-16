"""
AUTOR: Cauã Borges Faria, 834437
DATA DE CRIAÇÃO: 09/09/24
DATA DE MODIFICAÇÃO: 09/09/24
OBJETIVO: Realizar cálculos e operações de manipulação de círculos.
"""

import math

# Definindo classes para modelar o círculo:
class Ponto():
    def __init__(self, coordx=0, coordy=0):
        self.x = coordx
        self.y = coordy

class Circulo():
    def __init__(self, raio, p):
        self.raio = raio
        self.p = Ponto(p.x, p.y)
    
    def area(self):
        area = math.pi * self.raio**2
        return area

### Funções:

"""
Sub-rotina: lerCirculo
Objetivo: Inicializar um struct tCirculo com valores fornecidos pelo usuário
Valor de Retorno: circulo contendo coordenadas de um ponto e um raio
"""
def lerCirculo():
    raio = float(input("Raio: "))
    x = float(input("X: "))
    y = float(input("Y: "))
    ponto = Ponto(x, y)
    c = Circulo(raio, ponto)
    return c

"""
Sub-rotina: escreverCirculo
Objetivo: Mostrar ao usuário as informações contidas em um objeto tCirculo
Parâmetros:
- c: estrutura com raio e coordenadas de um ponto (entrada);
Valor de Retorno: NENHUM
"""
def escreverCirculo(c):
    print("Ponto:")
    print("X:", c.p.x)
    print("Y:", c.p.y)
    print("Raio:", c.raio)

"""
sub-rotina: areaCirculo
objetivo: calcular a área de um círculo.
parâmetros:
- c: estrutura com raio e coordenadas de um ponto (entrada);
valor de retorno: área do círculo
"""
def areaCirculo(c):
    PI = math.pi
    return PI*c.raio**2

"""
Sub-rotina: perimetroCirculo
Objetivo: Calcular o perímetro de um círculo.
Parâmetros:
- c: estrutura com raio e coordenadas de um ponto (entrada);
Valor de Retorno: perímetro do círculo
"""
def perimetroCirculo(c):
    PI = math.pi
    return 2*PI*c.raio

"""
Sub-rotina: distanciaCentroCirculos
Objetivo: Calcular a distância entre os centros de dois círculos
Parâmetros:
- c1: estrutura com raio e coordenadas de um ponto (entrada);
- c2: estrutura com raio e coordenadas de um ponto (entrada);
Valor de Retorno: distância entre os centros dos círculos
"""
def distanciaCentroCirculos(c1, c2):
    distancia = math.sqrt((c2.p.x - c1.p.x)**2 + (c2.p.y - c1.p.y)**2)
    return distancia

"""
Sub-rotina: distanciaMinimaCirculos
Objetivo: Calcular a distância mínima entre dois círculos
Parâmetros:
- c1: estrutura com raio e coordenadas de um ponto (entrada);
- c2: estrutura com raio e coordenadas de um ponto (entrada);
Valor de Retorno: distância mínima entre os círculos
"""
def distanciaMinimaCirculos(c1, c2):
    distanciaCentros = distanciaCentroCirculos(c1, c2)

    if (distanciaCentros <= (c1.raio + c2.raio)):
        distancia = 0
    else:
        distancia = abs(distanciaCentros - (c1.raio + c2.raio))

    return distancia

"""
Sub-rotina: deslocaCirculo
Objetivo: Deslocar o centro de um círculo com base nos parâmetros fornecidos
Parâmetros:
- c: estrutura com raio e coordenadas de um ponto (entrada e saída);
- x: valor a ser deslocado no eixo x (entrada);
- y: valor a ser deslocado no eixo y (entrada).
Valor de Retorno: NENHUM
"""
def deslocaCirculo(circulo, x, y):
    circulo.p.x += x
    circulo.p.y += y


# Inicializando círculo:
print("Círculo 1:")
c1 = lerCirculo()
escreverCirculo(c1)

# Cálculos de área e perímetro:
print("Área:", areaCirculo(c1))
print("Área método:", c1.area())
print("Perímetro:", perimetroCirculo(c1))

# Inicializando segundo círculo:
print("\nCírculo 2:")
c2 = lerCirculo()

# Cálculos relacionais entre círculos:
print("Distância entre centros de c1 e c2: %.2f" % distanciaCentroCirculos(c1, c2))
print("Distância mínima entre c1 e c2: %.2f" % distanciaMinimaCirculos(c1, c2))

# Deslocando círculo:
print("\nDeslocando c1:")
x = float(input("X: "))
y = float(input("Y: "))
deslocaCirculo(c1, x, y)
escreverCirculo(c1)
