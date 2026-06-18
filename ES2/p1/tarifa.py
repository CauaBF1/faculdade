def calcular_tarifa(distancia, urgente):
    tarifa = 12
    if distancia > 20:
        tarifa += 8
    if urgente:
        tarifa *= 2
    return tarifa

