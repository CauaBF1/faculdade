import pytest
from notas import calcular_media

def test_item_a():
    assert calcular_media([7,8,9]) == 8

def test_item_b():
    assert calcular_media([0,10]) == 5

def test_item_c():
    with pytest.raises(ValueError, match="lista vazia"):
        calcular_media([])

def test_item_d():
    with pytest.raises(ValueError, match="nota invalida"):
        calcular_media([-1,11])


'''
e) Para permitir que o pytest descubra automaticamente o arquivo e as funções de teste, as funções devem começar com 'test_' e o arquivo deve começar com 'test_' ou terminar com '_test'
'''
