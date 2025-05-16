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

        # Apenas o diâmetro é necessário como resultado final
        diameter, _ = helper(node)
        return diameter


if __name__ == "__main__":
    tree = BST()

    values = [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 5, 17, 19]

    for value in values:
        tree.tree_insert(value)
    
    print("Árvore:")
    tree.print_tree()

    print("\nDiâmetro da árvore:", tree.diameter())