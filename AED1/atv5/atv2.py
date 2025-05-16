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

    def replace_with_subtree_sum(self, node=None):
        if node is None:
            node = self.root
        
        def helper(n):
            if n is None:
                return 0
            left_sum = helper(n.left)
            right_sum = helper(n.right)
            old_val = n.key
            n.key = left_sum + right_sum
            return old_val + n.key
        
        helper(node)


if __name__ == "__main__":
    tree = BST()
    
    values = [16, 8, 24, 4, 12, 20, 28, 2, 6, 10, 14, 18, 22, 26, 30, 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31]
    for value in values:
        tree.tree_insert(value)

    print("Árvore original:")
    tree.print_tree()

    tree.replace_with_subtree_sum()

    print("\nÁrvore com os nós substituídos pela soma dos filhos:")
    tree.print_tree()

