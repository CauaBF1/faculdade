def calcular_status_pedido(valor_compra, quantidade_itens, cliente_vip):
    status = "normal"

    if valor_compra <= 0 or quantidade_itens <= 0:
        status = "invalido"
    else:
        if valor_compra >= 200:
            status = "frete gratis"

        if quantidade_itens >= 5:
            status = "prioritario"

        if cliente_vip and valor_compra >= 100:
            status = "vip"

    return status

