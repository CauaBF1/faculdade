import math

# Mapeamento de letras para seus códigos binários (inteiros)
LETTER_CODES = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    "E": 5,
    "F": 6,
    "G": 7,
    "H": 8,
    "I": 9,
    "J": 10,
    "K": 11,
    "L": 12,
    "M": 13,
    "N": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}

# Mapeamento inverso (código para letra) para plotagem
CODE_LETTERS = {v: k for k, v in LETTER_CODES.items()}

W = 5  # Número de bits para codificar as chaves


# Definição do nó da Trie (adaptado do uso no pseudocódigo)
class TrieNode:
    def __init__(self, key=None):
        self.key = key  # A chave (código inteiro da letra) armazenada neste nó
        self.children = [None, None]  # child[0] para bit 0, child[1] para bit 1
        self.parent = None  # Referência ao nó pai
        # Adicionamos um campo para a letra original para facilitar a plotagem
        self.letter = CODE_LETTERS.get(key, None) if key is not None else None


# Definição da Trie T
class Trie:
    def __init__(self):
        self.root = TrieNode()  # Raiz não armazena chave real


# Função para extrair o i-ésimo bit (0 a w-1) da chave k
# O pseudocódigo usa (k >> (w-1)-i) & 1
def get_bit(key, i, w):
    if key is None:  # Segurança
        return None
    # Shift para a direita para colocar o bit desejado na posição 0
    # i=0 -> shift w-1; i=1 -> shift w-2; ... ; i=w-1 -> shift 0
    shifted_key = key >> (w - 1 - i)
    # Retorna o bit menos significativo (posição 0)
    return shifted_key & 1


# Implementação da inserção na Trie (Trie_Insert)
# Adaptada para aceitar a letra, converter para código e criar o nó
def Trie_Insert(T, letter):
    key_code = LETTER_CODES.get(letter)
    if key_code is None:
        print(f"Erro: Letra '{letter}' inválida.")
        return False

    x = TrieNode(key_code)  # Cria o nó para a nova chave
    u = T.root
    parent_node = None
    insertion_bit = -1

    # Loop 'for i = 0 to w-1'
    for i in range(W):
        # c = (x.key >> (w-1)-i) & 1 # extrai bit a ser comparado
        c = get_bit(x.key, i, W)

        if u.key == x.key:
            # print(f"Chave {letter} ({x.key}) já existe na Trie.")
            return False  # chave já pertence a T

        # if u.child[c] == NIL
        if u.children[c] is None:
            # break # achou posição da chave
            parent_node = u
            insertion_bit = c
            break  # Encontrou o local de inserção
        else:
            # u = u.child[c]
            u = u.children[c]

    # Se o loop terminou sem break, significa que um nó existente
    # ocupa o caminho completo da chave a ser inserida. Isso não deveria
    # acontecer se as chaves forem únicas e inseridas corretamente.
    # No entanto, se break ocorreu:
    if parent_node is not None and insertion_bit != -1:
        # u.child[c] = x
        parent_node.children[insertion_bit] = x
        # x.p = u
        x.parent = parent_node
        # print(f"Inserido {letter} ({x.key}) como filho {insertion_bit} de {parent_node.key}")
        return True
    else:
        # Este caso pode indicar um problema: ou a chave já existe (mas não foi detectada
        # pela verificação u.key == x.key), ou o caminho está ocupado por outra chave.
        # A verificação u.key == x.key no meio do caminho é estranha.
        # ssumir que se o loop completou, a chave já existe ou há conflito.
        # print(f"Não foi possível inserir {letter} ({x.key}). Caminho completo ou chave existente?")
        # Tentativa de verificar se a chave existe no nó final 'u'
        if u.key == x.key:
            # print(f"Chave {letter} ({x.key}) já existe na Trie (detectado no final).")
            return False
        else:
            # print(f"Conflito de caminho ao inserir {letter} ({x.key}). Nó final: {u.key}")
            # Poderia acontecer se uma chave for prefixo de outra e inserida depois.
            # A estrutura da Trie da apostila parece colocar a chave no *primeiro* nó livre.
            return False  # Não inserido


# Implementação da remoção da Trie (Trie_Delete)
def Trie_Delete(T, letter):
    key_code = LETTER_CODES.get(letter)
    if key_code is None:
        print(f"Erro: Letra '{letter}' inválida para remoção.")
        return False

    u = T.root
    target_node = None
    target_bit_index = -1  # Índice do bit que levou ao nó a ser removido

    # Encontra o nó 'u' que contém a chave a ser removida
    # Loop 'for i = 0 to w-1'
    for i in range(W):
        # c = (x.key >> (w-1)-i) & 1 # extrai bit a ser comparado
        c = get_bit(key_code, i, W)

        if u.children[c] is None:
            # print(f"Chave {letter} ({key_code}) não encontrada (caminho interrompido).")
            return False  # chave não pertence a T

        # Avança para o filho
        u = u.children[c]

        # Verifica se o nó atual contém a chave
        if u.key == key_code:
            target_node = u
            target_bit_index = i  # Guarda o índice do último bit verificado
            break  # encontrou chave a ser removida

    # Se target_node não foi encontrado após o loop
    if target_node is None:
        # print(f"Chave {letter} ({key_code}) não encontrada na Trie.")
        return False

    # Verifica se o nó encontrado está na profundidade correta (w-1)
    # O pseudocódigo usa 'if i == w-1' após o loop para checar se é folha,
    # mas 'i' seria w se o loop completasse. checar se target_bit_index é w-1.
    is_leaf_position = target_bit_index == W - 1

    # Verifica se o nó é realmente uma folha na estrutura (sem filhos)
    is_structurally_leaf = (
        target_node.children[0] is None and target_node.children[1] is None
    )

    # Caso 1: Nó a ser removido é uma folha estrutural
    # O pseudocódigo checar apenas a profundidade (i == w-1).
    # seguir a lógica de ser uma folha estrutural, que é mais robusta.
    if is_structurally_leaf:
        # u.p.child[c] = NIL # desaloca o nó
        parent = target_node.parent
        if parent:
            # Descobre qual filho (0 ou 1) o target_node era
            bit_from_parent = get_bit(target_node.key, target_bit_index, W)
            # Correção: O bit que levou ao nó é o bit 'c' da iteração anterior do pai.
            # Precisamos do bit na profundidade do pai que levou a este nó.
            if target_bit_index >= 0:
                parent_depth_bit_index = target_bit_index
                bit_c = get_bit(target_node.key, parent_depth_bit_index, W)
                if parent.children[bit_c] == target_node:
                    parent.children[bit_c] = None
                    # print(f"Removido nó folha {letter} ({target_node.key}).")
                    return True
                else:
                    # Tentativa alternativa: verificar ambos os filhos do pai
                    if parent.children[0] == target_node:
                        parent.children[0] = None
                        # print(f"Removido nó folha {letter} ({target_node.key}).")
                        return True
                    elif parent.children[1] == target_node:
                        parent.children[1] = None
                        # print(f"Removido nó folha {letter} ({target_node.key}).")
                        return True
                    else:
                        # print(f"Erro: Não foi possível desconectar nó folha {letter} do pai.")
                        return False
            else:
                # print(f"Erro: target_bit_index inválido para nó folha {letter}.")
                return False
        else:
            # print(f"Erro: Nó folha {letter} não tem pai?") # Não deveria acontecer com raiz dummy
            return False

    # Caso 2: Nó a ser removido não é uma folha estrutural
    else:
        # se nó não é folha
        z = target_node  # Nó a ser substituído (u no pseudocódigo)
        replacement_leaf = None
        parent_of_leaf = None
        bit_leading_to_leaf = -1

        # Encontra um descendente que seja folha (preferindo esquerda)
        # while z.child[0] ≠ NIL or z.child[1] ≠ NIL
        current = z
        path_bits = []
        while current.children[0] is not None or current.children[1] is not None:
            # if z.child[0] ≠ NIL
            if current.children[0] is not None:
                # z = z.child[0]
                parent_of_leaf = current
                current = current.children[0]
                # c = 0 # vim da esquerda
                bit_leading_to_leaf = 0
                path_bits.append(0)
            # else
            else:
                # z = z.child[1]
                parent_of_leaf = current
                current = current.children[1]
                # c = 1 # vim da direita
                bit_leading_to_leaf = 1
                path_bits.append(1)

        replacement_leaf = current  # 'z' no pseudocódigo agora é a folha encontrada

        # u.key = z.key # atualiza chave do nó original com a chave da folha
        target_node.key = replacement_leaf.key
        target_node.letter = replacement_leaf.letter  # Atualiza a letra também

        # z.p.child[c] = NIL # desaloca o nó folha
        if parent_of_leaf and bit_leading_to_leaf != -1:
            parent_of_leaf.children[bit_leading_to_leaf] = None
            # print(f"Removido nó interno {letter}. Substituído por {replacement_leaf.letter}. Folha removida.")
            return True
        else:
            # print(f"Erro: Não foi possível remover a folha substituta {replacement_leaf.letter}.")
            # Isso pode acontecer se o nó a remover só tinha um filho, que era a folha.
            # Nesse caso, parent_of_leaf seria o próprio target_node.
            if target_node.children[bit_leading_to_leaf] == replacement_leaf:
                target_node.children[bit_leading_to_leaf] = None
                # print(f"Removido nó interno {letter}. Substituído por {replacement_leaf.letter}. Folha (filho direto) removida.")
                return True
            else:
                # print(f"Erro desconhecido ao remover folha substituta {replacement_leaf.letter}.")
                return False


# Função para calcular a altura h da árvore
def calculate_height(node):
    """Calcula a altura de uma subárvore (número de arestas no caminho mais longo)."""
    if node is None or (node.children[0] is None and node.children[1] is None):
        return 0  # Altura de folha ou subárvore vazia é 0

    left_height = calculate_height(node.children[0])
    right_height = calculate_height(node.children[1])

    return 1 + max(left_height, right_height)


# Função para plotar a árvore (adaptada de fontes online - simples)
def plot_trie(node, prefix="", is_left=True):
    """Imprime uma representação textual da Trie."""
    if node is None:
        return

    if node.parent is not None:  # Não imprime a raiz dummy
        branch = "└── " if is_left else "┌── "  # Invertido para visualização top-down
        key_str = (
            f"{node.letter}({node.key})" if node.key is not None else "(R)"
        )  # (R) para raiz
        print(prefix + branch + key_str)
        new_prefix = prefix + ("    " if is_left else "│   ")
    else:  # Raiz dummy
        print("(Raiz Dummy)")
        new_prefix = prefix

    # A ordem de impressão dos filhos importa para a visualização
    # Imprime filho direito (1) primeiro se existir
    if node.children[1]:
        plot_trie(node.children[1], new_prefix, False)
    # Imprime filho esquerdo (0) depois se existir
    if node.children[0]:
        plot_trie(node.children[0], new_prefix, True)


# --- Parte A ---
print("--- Questão 5: Parte A ---")
T = Trie()
insertion_order = [
    "P",
    "L",
    "O",
    "M",
    "D",
    "V",
    "F",
    "U",
    "X",
    "J",
    "I",
    "A",
    "S",
    "W",
    "Q",
    "T",
    "K",
    "B",
    "N",
    "Z",
    "E",
    "Y",
    "R",
    "C",
    "H",
    "G",
]

print(f"Ordem de inserção: {' '.join(insertion_order)}")
inserted_count = 0
for letter in insertion_order:
    if Trie_Insert(T, letter):
        inserted_count += 1
print(f"Inseridas {inserted_count} chaves.")

# Calcular altura h
h_a = calculate_height(T.root)
print(f"Altura h da árvore resultante (Parte A): {h_a}")

# Comparar com w=5 e log2(n)
n = len(insertion_order)
log2_n = math.log2(n) if n > 0 else 0
print(f"Comparação: w = {W}, log2(n) = log2({n}) ≈ {log2_n:.2f}")
if abs(h_a - W) < abs(h_a - log2_n):
    print(f"A altura h={h_a} é mais próxima de w={W}.")
elif abs(h_a - log2_n) < abs(h_a - W):
    print(f"A altura h={h_a} é mais próxima de log2(n)≈{log2_n:.2f}.")
else:
    print(
        f"A altura h={h_a} é equidistante de w={W} e log2(n)≈{log2_n:.2f} (ou um deles é igual a h)."
    )

# Plotar árvore resultante (Parte A)
print("\nPlot da Árvore (Parte A):")
plot_trie(T.root)

# --- Parte B ---
print("\n--- Questão 5: Parte B ---")
removal_keys = ["A", "E", "I", "O", "U", "K", "X", "W", "Z"]
print(f"Chaves a remover: {' '.join(removal_keys)}")

removed_count = 0
for letter in removal_keys:
    if Trie_Delete(T, letter):
        removed_count += 1
print(f"Removidas {removed_count} chaves.")

# Calcular altura h após remoção
h_b = calculate_height(T.root)
print(f"Altura h da árvore resultante (Parte B): {h_b}")

# Plotar árvore resultante (Parte B)
print("\nPlot da Árvore (Parte B):")
plot_trie(T.root)
