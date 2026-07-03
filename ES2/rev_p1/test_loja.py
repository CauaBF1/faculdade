import pytest
from loja import Produto, aplicar_desconto

def test_random_atributos_produto():
    p = Produto("Carro", 10, 2)
    assert p.nome == "Carro"
    assert p.preco == 10
    assert p.quantidade == 2

def test_standart_atributos_produto():
    p = Produto("Bike", 5)
    assert p.nome == "Bike"
    assert p.preco == 5
    assert p.quantidade == 1

def test_subtotal_produto():
    p = Produto("Carro", 10, 2)
    assert p.subtotal == 20

def test_produtos_iguais():
    p = Produto("Carro", 10, 2)
    y = Produto("Carro", 10, 2)
    assert p == y

def test_produtos_diferentes():
    p = Produto("Carro", 10, 2)
    y = Produto("Bike", 10, 2)
    assert p != y

def test_cupom_10():
    assert aplicar_desconto(100, "ALUNO10") == 90

def test_cupom_20():
    assert aplicar_desconto(100, "ES2") == 80

def test_cupom_invalido():
    assert aplicar_desconto(100, "X") == 100

def test_preco_neg():
    p = Produto("Carro", -10)
    with pytest.raises(ValueError):
        p.subtotal

def test_quant_neg():
    p = Produto("Carro", 10, -1)
    with pytest.raises(ValueError):
        p.subtotal

'''
Sim, encontra arquivos q começam ou terminam com _test ou _test
Não, precisa começar com test_
pytest -k desconto
'''


