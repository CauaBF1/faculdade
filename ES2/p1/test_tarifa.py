from tarifa import calcular_tarifa

def test_entrega_longa_urgente():
    assert calcular_tarifa(30, True) == 40

# Item d
def test_entrega_curta_nao_urgente():
    assert calcular_tarifa(20, False) == 12
# o test_entrega_loga_urgente cobre os desvios True, True, enquanto o test_entrega_curta_nao_urgente cobre os desvios False, False. Não é necessário fazer cobrindo [True, False] ou [False, True], isso pode ser validado rodando ´pytest --cov=tarifa --cov-branch --cov-report=term-missing test_tarifa.py´, o qual retorna cover 100%


