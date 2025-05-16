"""
AUTOR: Cauã Borges Faria
DATA DE CRIAÇÃO: 10/09/24
DATA DE MODIFICAÇÃO: 10/09/24
OBJETIVO: Realizar operações de manipulação de conjuntos, incluindo verificação de inclusão, igualdade e operações básicas.
"""

class Conjunto:

    """
    Construtor da classe Conjunto.
    Objetivo: Inicializar um conjunto com elementos fornecidos ou um conjunto vazio.
    Parâmetros:
    - elementos: lista de elementos iniciais do conjunto (opcional).
    """
    def __init__(self, elementos=None):
        if elementos is None:
            self.elementos = set()
        else:
            self.elementos = set(elementos)

    """
    Adiciona um elemento ao conjunto.
    Parâmetros:
    - elemento: o elemento a ser adicionado.
    Valor de Retorno: NENHUM
    """
    def adicionar(self, elemento):
        self.elementos.add(elemento)

    """
    Remove um elemento do conjunto.
    Parâmetros:
    - elemento: o elemento a ser removido.
    Valor de Retorno: NENHUM
    """
    def remover(self, elemento):
        self.elementos.discard(elemento)  # Não levanta exceção se o elemento não estiver presente

    """
    Retorna o número de elementos no conjunto.
    Valor de Retorno: Tamanho do conjunto (int).
    """
    def tamanho(self):
        return len(self.elementos)

    """
    Verifica se um elemento pertence ao conjunto.
    Parâmetros:
    - elemento: o elemento a ser verificado.
    Valor de Retorno: True se o elemento estiver no conjunto, False caso contrário.
    """
    def pertence(self, elemento):
        return elemento in self.elementos

    """
    Verifica se o conjunto está contido em outro conjunto.
    Parâmetros:
    - outro_conjunto: o conjunto a ser verificado.
    Valor de Retorno: True se o conjunto estiver contido em outro_conjunto, False caso contrário.
    """
    def esta_contido_em(self, outro_conjunto):
        return self.elementos.issubset(outro_conjunto.elementos)

    """
    Verifica se dois conjuntos são iguais.
    Parâmetros:
    - outro_conjunto: o conjunto a ser comparado.
    Valor de Retorno: True se os conjuntos forem iguais, False caso contrário.
    """
    def igual(self, outro_conjunto):
        return self.elementos == outro_conjunto.elementos

    """
    Retorna a união de dois conjuntos.
    Parâmetros:
    - outro_conjunto: o conjunto a ser unido com o conjunto atual.
    Valor de Retorno: Novo Conjunto que é a união dos dois conjuntos.
    """
    def uniao(self, outro_conjunto):
        return Conjunto(self.elementos.union(outro_conjunto.elementos))

    """
    Retorna a interseção de dois conjuntos.
    Parâmetros:
    - outro_conjunto: o conjunto a ser intersectado com o conjunto atual.
    Valor de Retorno: Novo Conjunto que é a interseção dos dois conjuntos.
    """
    def interseccao(self, outro_conjunto):
        return Conjunto(self.elementos.intersection(outro_conjunto.elementos))

    """
    Retorna a diferença entre dois conjuntos.
    Parâmetros:
    - outro_conjunto: o conjunto a ser subtraído do conjunto atual.
    Valor de Retorno: Novo Conjunto que é a diferença entre os dois conjuntos.
    """
    def diferenca(self, outro_conjunto):
        return Conjunto(self.elementos.difference(outro_conjunto.elementos))

    """
    Representa o conjunto como uma string.
    Valor de Retorno: String representando o conjunto.
    """
    def __str__(self):
        return f"Conjunto({self.elementos})"


"""
Lê os elementos de um conjunto a partir da entrada do usuário.
Objetivo: Inicializar um Conjunto com valores fornecidos pelo usuário.
Valor de Retorno: Conjunto contendo os elementos fornecidos.
"""
def ler_conjunto():
    elementos = input("Digite os elementos do conjunto separados por espaço: ")
    lista_elementos = elementos.split()
    return Conjunto(lista_elementos)


"""
Exibe as informações de um conjunto para o usuário.
Parâmetros:
- conjunto: o conjunto a ser exibido.
Valor de Retorno: NENHUM
"""
def escrever_conjunto(conjunto):
    print(f"Conjunto: {conjunto}")


# Inicializando conjuntos:
print("Conjunto 1:")
c1 = ler_conjunto()
escrever_conjunto(c1)

# Inicializando segundo conjunto:
print("\nConjunto 2:")
c2 = ler_conjunto()
escrever_conjunto(c2)

# Operações entre conjuntos:
print("\nOperações entre conjuntos:")
print(f"Conjunto 1 está contido em Conjunto 2: {c1.esta_contido_em(c2)}")
print(f"Conjunto 1 é igual ao Conjunto 2: {c1.igual(c2)}")

uniao = c1.uniao(c2)
print(f"União de Conjunto 1 e Conjunto 2: {uniao}")

interseccao = c1.interseccao(c2)
print(f"Interseção de Conjunto 1 e Conjunto 2: {interseccao}")

diferenca = c1.diferenca(c2)
print(f"Diferença de Conjunto 1 e Conjunto 2: {diferenca}")

