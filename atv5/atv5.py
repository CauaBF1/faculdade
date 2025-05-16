class TreeNode:
    def __init__(self, key):
        self.key = key
        self.p = None
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)

class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def tree_insert(self, key):
        new_node = TreeNode(key)
        y = None
        x = self.root

        while x is not None:
            y = x
            if new_node.key < x.key:
                x = x.left
            else:
                x = x.right

        new_node.p = y
        if y is None:
            self.root = new_node
        elif new_node.key < y.key:
            y.left = new_node
        else:
            y.right = new_node

        self.size += 1

    def print_tree(self, node=None, prefix="", is_left=True):
        if node is None:
            node = self.root

        if node.right is not None:
            self.print_tree(node.right, prefix + ("│   " if is_left else "    "), False)
        
        print(prefix + ("└── " if is_left else "┌── ") + str(node.key))
        
        if node.left is not None:
            self.print_tree(node.left, prefix + ("    " if is_left else "│   "), True)

    def search(self, node, key):
        while node is not None and key != node.key:
            if key < node.key:
                node = node.left
            else:
                node = node.right
        return node  # Retorna o nó encontrado ou None se não estiver na árvore


    def diameter(self, node=None):
        if node is None:
            node = self.root

        def helper(n):
            if n is None:
                return 0, -1  # Retorna (diâmetro, altura)

            # Calcula o diâmetro e a altura das subárvores esquerda e direita
            left_diameter, left_height = helper(n.left)
            right_diameter, right_height = helper(n.right)

            # Calcula a altura atual
            current_height = max(left_height, right_height) + 1

            # Calcula o diâmetro atual (caminho que passa pela raiz)
            current_diameter = left_height + right_height + 2

            # O diâmetro final é o maior entre os três valores
            max_diameter = max(left_diameter, right_diameter, current_diameter)

            return max_diameter, current_height

        # Só o diâmetro é necessário como resultado
        diameter, _ = helper(node)
        return diameter

    def is_balanced(self, node=None):
        if node is None:
            node = self.root

        def helper(n):
            if n is None:
                return True, -1  # Árvore vazia é balanceada e tem altura -1

            # Verifica se as subárvores esquerda e direita são balanceadas
            left_balanced, left_height = helper(n.left)
            right_balanced, right_height = helper(n.right)

            # Calcula a altura atual
            current_height = max(left_height, right_height) + 1

            # Verifica se o nó atual é balanceado
            is_current_balanced = abs(left_height - right_height) <= 1

            # A árvore inteira é balanceada se as subárvores são balanceadas e o nó atual também
            is_tree_balanced = left_balanced and right_balanced and is_current_balanced

            return is_tree_balanced, current_height

        # Só o valor booleano indicando se a árvore é balanceada
        balanced, _ = helper(node)
        return balanced

if __name__ == "__main__":
    tree = BST()
    tree2 = BST()
    values = [16, 8, 24, 4, 12, 20, 28, 2, 10, 14, 18, 22, 26, 17, 19]
    values2 = [16, 8, 24, 12, 20, 10, 14, 18, 22, 17, 19]

    for value in values:
        tree.tree_insert(value)
    
    for value in values2:
        tree2.tree_insert(value)
    
    print("Árvore 1:")
    tree.print_tree()

    print("\nÁrvore 2:")
    tree2.print_tree()

    print("\nArvore 1 é balanceada?", tree.is_balanced())
    print("Arvore 2 é balanceada?", tree2.is_balanced())