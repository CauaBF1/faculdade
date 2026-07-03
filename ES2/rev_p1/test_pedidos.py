import pytest
from pedidos import calcular_status_pedido

def test_valor_invalido():
    assert calcular_status_pedido(0,0,True) == "invalido"

def test_standart():
    assert calcular_status_pedido(10, 1, False) == "normal"

def test_gratis():
    assert calcular_status_pedido(200, 1, False) == "frete gratis"

def test_prioritario():
    assert calcular_status_pedido(10, 5, False) == "prioritario"

def test_vip():
    assert calcular_status_pedido(100, 1, True) == "vip"


