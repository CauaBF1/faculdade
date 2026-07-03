import pytest

@pytest.fixture
def retorna_valor_universo():
    return 42

def test_valor_univ(retorna_valor_universo):
    assert 42 == retorna_valor_universo
