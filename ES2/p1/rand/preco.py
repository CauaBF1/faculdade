def calcular_preco_final(preco, cliente_vip):
    desconto = 0
    if cliente_vip:
        desconto = preco * 0.50
    return preco - desconto
