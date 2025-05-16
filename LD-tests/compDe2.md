## Complemento de 2
---
ara converter de binário para decimal (com sinal):

    Identifique o bit mais significativo (MSB):
        Se o MSB for 0, o número é positivo e você pode converter diretamente de binário para decimal.
        Se o MSB for 1, o número é negativo e você deve usar o complemento de 2 para encontrar seu valor decimal.

    Se o número for negativo (MSB = 1):
        Inverta todos os bits do número.
        Some 1 ao resultado.
        Converta o resultado para decimal e coloque um sinal negativo na frente.

Para converter de decimal para binário (com sinal):

    Se o número for positivo:
        Converta diretamente de decimal para binário e complete com zeros à esquerda para obter 4 bits.

    Se o número for negativo:
        Converta o valor absoluto do número para binário.
        Inverta todos os bits do resultado.
        Some 1 ao resultado.
        Complete com zeros à esquerda para obter 4 bits.

Aplicando ao Exemplo
Dado na tabela:

Para a quinta linha da tabela:

    a(2): 0100 (fornecido)
    a(10): 4 (conversão de 0100 para decimal)
    op: 0 (soma, fornecido)
    y(2): 0001 (fornecido)
    y(10): 1 (conversão de 0001 para decimal)

Queremos determinar b(2) e b(10).
Encontrando b(2) e b(10):

Sabemos que a+b=ya+b=y:

    a = 4
    y = 1
    op = 0 (soma)

Portanto:

4+b=14+b=1
b=1−4b=1−4
b=−3b=−3

Converter -3 para binário (complemento de 2):

    Converta 3 para binário: 3 é 0011.
    Inverta todos os bits: 0011 -> 1100.
    Some 1: 1100 + 1 = 1101.

Portanto:

    b(2) = 1101
    b(10) = -3

Verificação dos Outros Valores:

    nb(2): nb é o complemento de b. b(2) = 1101 -> nb(2) = 0010.
    nb(10): 0010 em decimal é 2.
