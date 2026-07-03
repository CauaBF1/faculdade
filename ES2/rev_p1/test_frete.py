from frete import calcular_frete

def test_frete_gratis():
    assert calcular_frete(100, True) == 0

def test_frete_vip():
    assert calcular_frete(80, True) == 10

def test_frete_padrao():
    assert calcular_frete(80, False) == 20


