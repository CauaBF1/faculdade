# -*- coding: utf-8 -*-
import random

class SkipListNode:
    def __init__(self, key, value, level):
        self.key = key
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level, p):
        self.max_level = max_level
        self.p = p
        self.header = self._create_node(None, None, max_level)
        self.level = 0

    def _create_node(self, key, value, level):
        return SkipListNode(key, value, level)

    def _random_level(self):
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def insert(self, key, value):
        update = [None] * (self.max_level + 1)
        current = self.header

        # Localizar posições onde os ponteiros devem ser atualizados
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.key == key:
            # Atualiza valor se a chave já existir
            current.value = value
        else:
            new_level = self._random_level()

            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.header
                self.level = new_level

            new_node = self._create_node(key, value, new_level)

            for i in range(new_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

    def search(self, key):
        current = self.header
        path = []
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                path.append(f"Nível {i}: Moveu de {current.key if current.key is not None else 'Cabeçalho'} para {current.forward[i].key}")
                current = current.forward[i]
            path.append(f"Nível {i}: Em {current.key if current.key is not None else 'Cabeçalho'}, próximo é {current.forward[i].key if current.forward[i] else 'Nenhum'}")

        current = current.forward[0]
        if current and current.key == key:
            path.append(f"Chave {key} encontrada com valor {current.value}")
            return current.value, path
        else:
            path.append(f"Chave {key} não encontrada.")
            return None, path

    def delete(self, key):
        update = [None] * (self.max_level + 1)
        current = self.header

        # Localizar posições onde os ponteiros devem ser atualizados
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].key < key:
                current = current.forward[i]
            update[i] = current

        current = current.forward[0]

        if current and current.key == key:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and not self.header.forward[self.level]:
                self.level -= 1
            return True
        return False

    def display(self):
        print("Lista Skip:")
        for i in range(self.level, -1, -1):
            print(f"Nível {i}: ", end="")
            node = self.header.forward[i]
            while node:
                print(f"({node.key}, {node.value}) ", end="")
                node = node.forward[i]
            print("")

# Execução principal — Questão 2 - Parte A
if __name__ == "__main__":
    # Definir semente fixa para gerar níveis aleatórios de forma reproduzível
    random.seed(42)

    # Inicializar a SkipList com nível máximo 3 e p=0.5 (valor comum)
    skip_list = SkipList(max_level=3, p=0.5)

    books = [
        (101, "Algoritmos e Estruturas de Dados"),
        (29, "Inteligencia Artificial"),
        (203, "Machine Learning Avancado"),
        (88, "Programacao em Python"),
        (175, "Redes Neurais e Deep Learning"),
        (256, "Sistemas Distribuidos"),
        (191, "Visao Computacional"),
        (317, "Logica Matematica"),
        (125, "Banco de Dados"),
        (297, "Sistemas Operacionais"),
        (410, "Redes de Computadores"),
        (281, "Compiladores"),
        (373, "Matematica Discreta"),
        (182, "Processamento Digital de Imagens"),
        (299, "Projeto e Analise de Algoritmos"),
        (437, "Engenharia de Software")
    ]

    print("Inserindo livros na Skip List:")
    for code, title in books:
        skip_list.insert(code, title)
        print(f"Inserido: ({code}, '{title}')")

    print("\nEstrutura final da Skip List:")
    skip_list.display()

    # Questão 2 - Parte B: Operações

    print("\n--- Questão 2 - Parte B: Operações ---")

    # Inserção de um novo livro
    new_book_key = 408
    new_book_title = "Processamento de Linguagem Natural"
    print(f"\nInserindo novo livro: ({new_book_key}, '{new_book_title}')")
    skip_list.insert(new_book_key, new_book_title)
    print("Skip List após nova inserção:")
    skip_list.display()

    # Busca pelo livro (373, "Matematica Discreta")
    search_key_1 = 373
    print(f"\nBuscando chave: {search_key_1}")
    value_1, path_1 = skip_list.search(search_key_1)
    print("Caminho percorrido:")
    for step in path_1:
        print(step)
    if value_1:
        print(f"Encontrado: ({search_key_1}, '{value_1}')")
    else:
        print(f"Chave {search_key_1} não encontrada.")

    # Busca pelo livro (400, "Teoria dos Grafos")
    search_key_2 = 400
    print(f"\nBuscando chave: {search_key_2}")
    value_2, path_2 = skip_list.search(search_key_2)
    print("Caminho percorrido:")
    for step in path_2:
        print(step)
    if value_2:
        print(f"Encontrado: ({search_key_2}, '{value_2}')")
    else:
        print(f"Chave {search_key_2} não encontrada.")

    # Remoção do livro "Machine Learning Avancado" (chave 203)
    remove_key = 203
    print(f"\nRemovendo chave: {remove_key} ('Machine Learning Avancado')")
    if skip_list.delete(remove_key):
        print(f"Chave {remove_key} removida com sucesso.")
    else:
        print(f"Chave {remove_key} não encontrada para remoção.")
    print("Skip List após remoção:")
    skip_list.display()
