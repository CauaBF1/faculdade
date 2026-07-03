def calcular_frete(valor_compra, cliente_vip): 
    frete = 20

    if valor_compra >= 100: 
       frete = 0
#       return frete

    if cliente_vip: 
        frete = frete / 2
    
    return frete


