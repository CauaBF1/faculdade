import pytest
from tarefas import ListaTarefas

@pytest.fixture
def lista_vazia():
    lista = ListaTarefas()
    print("teste antes")
    yield lista
    print("test depois")
    lista.limpar()

@pytest.fixture
def tarefas_prontas():
    return [("test1", "caua"), ("test2", "caua"), ("test3", "caua")]


@pytest.fixture
def lista_com_tarefas(lista_vazia, tarefas_prontas):
    for titulo, responsavel in tarefas_prontas:
        lista_vazia.adicionar(titulo, responsavel)
    # preciso retornar a lista, não basta adicionar tudo na lista se ela não vai ser retornada para eu testar
    return lista_vazia


def test_lista_comeca_vazia(lista_vazia):
    assert lista_vazia.contar() == 0

def test_adicionar2_count(lista_vazia):
    lista_vazia.adicionar("test1")
    lista_vazia.adicionar("test2")
    assert lista_vazia.contar() == 2

def test_duas_fixtures(lista_vazia, tarefas_prontas):
    for titulo, responsavel in tarefas_prontas:
        lista_vazia.adicionar(titulo, responsavel)

    assert lista_vazia.contar() == 3

def test_lista_com_tarefas(lista_com_tarefas):
    assert lista_com_tarefas.contar() != 0


'''
a)  O que acontece antes do yield?
acontece o setup, preparação da fixture

b) O que acontece depois do yield?
acontece o teardown, limpeza

c) Se lista_vazia usar scope="function", quantas vezes ela será executada?
uma vez para cada teste q usar ela

d) Se usar scope="module", qual cuidado você precisa ter?
usando module a mesma instancia é compartilhada para outros testes, o cuidado é evitar que um teste deixe estado acumulado para outro

'''


