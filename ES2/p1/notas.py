def calcular_media(notas):
    if not notas:
        raise ValueError("lista vazia")
    if any(nota < 0 or nota > 10 for nota in notas):
        raise ValueError("nota invalida")
    return sum(notas) / len(notas)

