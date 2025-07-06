'''
Cauã Borges Faria (834437)
Projeto de Algoritmo e Estrutura de Dados 2- Sistema de Gerenciamento de Transações Bancárias com Árvore AVL
Adicionado o account para representar a conta associada à transação.

'''

import math
import random
import time
from typing import List, Optional


class Transaction:
    """Classe para representar uma transação bancária."""

    def __init__(
        self,
        time: int,
        transaction_id: int = None,
        amount: float = None,
        transaction_type: str = None,
        account: str = None,
    ):
        self.time = time
        self.transaction_id = (
            transaction_id if transaction_id else random.randint(1000, 999999)
        )
        self.amount = amount if amount else round(random.uniform(10.0, 10000.0), 2)
        self.transaction_type = (
            transaction_type
            if transaction_type
            else random.choice(["DEPOSITO", "SAQUE"])
        )
        self.account = account if account else f"ACC{random.randint(1000, 9999)}"

    def __str__(self):
        return f"Time: {self.time}, ID: {self.transaction_id}, Amount: ${self.amount:.2f}, Type: {self.transaction_type}, Account: {self.account}"


class AVLNode:
    """Nó da árvore AVL."""

    def __init__(self, transaction: Transaction):
        self.transaction = transaction
        self.left: Optional["AVLNode"] = None
        self.right: Optional["AVLNode"] = None
        self.height = 1
        self.parent: Optional["AVLNode"] = None


class AVLTree:
    """Implementação da Árvore AVL para gerenciamento de transações bancárias."""

    def __init__(self):
        self.root: Optional[AVLNode] = None
        self.size = 0

    def height(self, node: Optional[AVLNode]) -> int:
        """Retorna a altura do nó."""
        if node is None:
            return 0
        return node.height

    def balance_factor(self, node: Optional[AVLNode]) -> int:
        """Calcula o fator de balanceamento do nó."""
        if node is None:
            return 0
        return self.height(node.left) - self.height(node.right)

    def update_height(self, node: AVLNode) -> None:
        """Atualiza a altura do nó."""
        node.height = 1 + max(self.height(node.left), self.height(node.right))

    def right_rotate(self, y: AVLNode) -> AVLNode:
        """Rotação à direita."""
        x = y.left
        beta = x.right

        # Executa a rotação
        x.right = y
        y.left = beta

        # Atualiza os pais
        x.parent = y.parent
        y.parent = x
        if beta:
            beta.parent = y

        # Atualiza alturas
        self.update_height(y)
        self.update_height(x)

        return x

    def left_rotate(self, x: AVLNode) -> AVLNode:
        """Rotação à esquerda."""
        y = x.right
        beta = y.left

        # Executa a rotação
        y.left = x
        x.right = beta

        # Atualiza os pais
        y.parent = x.parent
        x.parent = y
        if beta:
            beta.parent = x

        # Atualiza alturas
        self.update_height(x)
        self.update_height(y)

        return y

    def left_right_rotate(self, z: AVLNode) -> AVLNode:
        """Rotação esquerda-direita."""
        z.left = self.left_rotate(z.left)
        return self.right_rotate(z)

    def right_left_rotate(self, z: AVLNode) -> AVLNode:
        """Rotação direita-esquerda."""
        z.right = self.right_rotate(z.right)
        return self.left_rotate(z)

    def insert(self, transaction: Transaction) -> None:
        """Insere uma nova transação na árvore AVL."""
        self.root = self._insert_recursive(self.root, transaction)
        self.size += 1

    def _insert_recursive(
        self, node: Optional[AVLNode], transaction: Transaction
    ) -> AVLNode:
        """Inserção recursiva com balanceamento."""
        # Inserção normal da BST
        if node is None:
            return AVLNode(transaction)

        if transaction.time < node.transaction.time:
            node.left = self._insert_recursive(node.left, transaction)
            if node.left:
                node.left.parent = node
        elif transaction.time > node.transaction.time:
            node.right = self._insert_recursive(node.right, transaction)
            if node.right:
                node.right.parent = node
        else:
            # Chave já existe, não insere
            return node

        # Atualiza altura
        self.update_height(node)

        # Obtém fator de balanceamento
        balance = self.balance_factor(node)

        # Casos de rotação
        # Caso 1: Rotação à direita
        if balance > 1 and transaction.time < node.left.transaction.time:
            return self.right_rotate(node)

        # Caso 2: Rotação à esquerda
        if balance < -1 and transaction.time > node.right.transaction.time:
            return self.left_rotate(node)

        # Caso 3: Rotação esquerda-direita
        if balance > 1 and transaction.time > node.left.transaction.time:
            return self.left_right_rotate(node)

        # Caso 4: Rotação direita-esquerda
        if balance < -1 and transaction.time < node.right.transaction.time:
            return self.right_left_rotate(node)

        return node

    def search(self, time: int) -> Optional[Transaction]:
        """Busca uma transação pelo tempo."""
        return self._search_recursive(self.root, time)

    def _search_recursive(
        self, node: Optional[AVLNode], time: int
    ) -> Optional[Transaction]:
        """Busca recursiva."""
        if node is None:
            return None

        if time == node.transaction.time:
            return node.transaction
        elif time < node.transaction.time:
            return self._search_recursive(node.left, time)
        else:
            return self._search_recursive(node.right, time)

    def delete(self, time: int) -> bool:
        """Remove uma transação da árvore."""
        if self.search(time) is None:
            return False

        self.root = self._delete_recursive(self.root, time)
        self.size -= 1
        return True

    def _delete_recursive(
        self, node: Optional[AVLNode], time: int
    ) -> Optional[AVLNode]:
        """Remoção recursiva com balanceamento."""
        if node is None:
            return None

        # Busca o nó a ser removido
        if time < node.transaction.time:
            node.left = self._delete_recursive(node.left, time)
        elif time > node.transaction.time:
            node.right = self._delete_recursive(node.right, time)
        else:
            # Nó encontrado
            # Caso 1: Nó folha ou com um filho
            if node.left is None:
                temp = node.right
                if temp:
                    temp.parent = node.parent
                return temp
            elif node.right is None:
                temp = node.left
                if temp:
                    temp.parent = node.parent
                return temp

            # Caso 2: Nó com dois filhos
            # Encontra o sucessor (menor nó da subárvore direita)
            successor = self._find_min(node.right)

            # Substitui o conteúdo do nó
            node.transaction = successor.transaction

            # Remove o sucessor
            node.right = self._delete_recursive(node.right, successor.transaction.time)

        # Atualiza altura
        self.update_height(node)

        # Obtém fator de balanceamento
        balance = self.balance_factor(node)

        # Casos de rotação
        # Caso 1: Rotação à direita
        if balance > 1 and self.balance_factor(node.left) >= 0:
            return self.right_rotate(node)

        # Caso 2: Rotação esquerda-direita
        if balance > 1 and self.balance_factor(node.left) < 0:
            return self.left_right_rotate(node)

        # Caso 3: Rotação à esquerda
        if balance < -1 and self.balance_factor(node.right) <= 0:
            return self.left_rotate(node)

        # Caso 4: Rotação direita-esquerda
        if balance < -1 and self.balance_factor(node.right) > 0:
            return self.right_left_rotate(node)

        return node

    def _find_min(self, node: AVLNode) -> AVLNode:
        """Encontra o nó com menor valor."""
        while node.left is not None:
            node = node.left
        return node

    def get_tree_height(self) -> int:
        """Retorna a altura da árvore."""
        return self.height(self.root)

    def in_order_traversal(self) -> List[Transaction]:
        """Percurso em ordem (in-order) para listar transações ordenadas."""
        result = []
        self._in_order_recursive(self.root, result)
        return result

    def _in_order_recursive(
        self, node: Optional[AVLNode], result: List[Transaction]
    ) -> None:
        """Percurso em ordem recursivo."""
        if node is not None:
            self._in_order_recursive(node.left, result)
            result.append(node.transaction)
            self._in_order_recursive(node.right, result)


class BankingSystem:
    """Sistema de Gerenciamento de Transações Bancárias."""

    def __init__(self):
        self.avl_tree = AVLTree()
        self.current_time = 0

    def add_transaction(
        self, amount: float = None, transaction_type: str = None, account: str = None
    ) -> Transaction:
        """Adiciona uma nova transação ao sistema."""
        transaction = Transaction(
            self.current_time,
            amount=amount,
            transaction_type=transaction_type,
            account=account,
        )
        self.avl_tree.insert(transaction)
        self.current_time += 1
        return transaction

    def search_transaction(self, time: int) -> Optional[Transaction]:
        """Busca uma transação específica pelo tempo."""
        return self.avl_tree.search(time)

    def remove_transaction(self, time: int) -> bool:
        """Remove uma transação específica."""
        return self.avl_tree.delete(time)

    def get_ordered_transactions(self) -> List[Transaction]:
        """Retorna todas as transações em ordem cronológica."""
        return self.avl_tree.in_order_traversal()

    def get_tree_height(self) -> int:
        """Retorna a altura da árvore."""
        return self.avl_tree.get_tree_height()

    def get_total_transactions(self) -> int:
        """Retorna o número total de transações."""
        return self.avl_tree.size


def main():
    """Função principal para executar o projeto."""
    print("🏦 Sistema de Gerenciamento de Transações Bancárias com Árvore AVL 🏦")
    print("=" * 80)

    # Inicializa o sistema
    banking_system = BankingSystem()

    # 1. Inserção de 5000 transações
    print("\n1. Inserindo 5000 transações...")
    start_time = time.time()

    for i in range(5000):
        banking_system.add_transaction()

    insertion_time = time.time() - start_time
    print(f"✅ 5000 transações inseridas em {insertion_time:.4f} segundos")
    print(f"📊 Altura da árvore após inserções: {banking_system.get_tree_height()}")

    # 2. Busca por tempos específicos
    print("\n2. Buscando transações específicas...")
    search_keys = [100, 1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 4999]

    start_time = time.time()
    found_transactions = []

    for key in search_keys:
        transaction = banking_system.search_transaction(key)
        if transaction:
            found_transactions.append(transaction)

    search_time = time.time() - start_time
    print(
        f"✅ Busca por {len(search_keys)} chaves concluída em {search_time:.6f} segundos"
    )
    print(f"📝 Transações encontradas: {len(found_transactions)}")


    # Exibe todas as transações encontradas
    print("\n🔍 Todas as transações encontradas:")
    for i, transaction in enumerate(found_transactions):
        print(f"  {i+1}. {transaction}")

    # 3. Remoção de transações antigas (tempo 0 a 500)
    print("\n3. Removendo transações antigas (tempo 0 a 500)...")
    start_time = time.time()

    removed_count = 0
    for time_to_remove in range(501):  # 0 a 500
        if banking_system.remove_transaction(time_to_remove):
            removed_count += 1

    removal_time = time.time() - start_time
    print(f"✅ {removed_count} transações removidas em {removal_time:.4f} segundos")
    print(f"📊 Altura da árvore após remoções: {banking_system.get_tree_height()}")
    print(
        f"📊 Total de transações restantes: {banking_system.get_total_transactions()}"
    )
    '''altura continuou a mesma, pois a presença de transações mais novas na parte a direita mantem a altura mesmo com a remoção de transações mais antigas na parte esquerda, e balancemnto da árvore.'''

    # 4. Exibição ordenada das transações restantes
    print("\n4. Exibindo transações em ordem cronológica...")
    ordered_transactions = banking_system.get_ordered_transactions()

    print(f"📝 Total de transações ordenadas: {len(ordered_transactions)}")
    print("\n🗂️ Primeiras 10 transações restantes:")
    for i, transaction in enumerate(ordered_transactions[:10]):
        print(f"  {i+1}. {transaction}")

    # Estatísticas finais
    print("\n" + "=" * 80)
    print("📊 ESTATÍSTICAS FINAIS")
    print("=" * 80)
    print(f"🏗️  Altura inicial da árvore: {banking_system.get_tree_height()}")
    print(f"⚡ Tempo de inserção de 5000 transações: {insertion_time:.4f} segundos")
    print(f"🔍 Tempo de busca por 10 chaves: {search_time:.6f} segundos")
    print(f"🗑️  Tempo de remoção de 501 transações: {removal_time:.4f} segundos")
    print(f"📊 Transações restantes: {banking_system.get_total_transactions()}")
    print(f"📏 Altura final da árvore: {banking_system.get_tree_height()}")

    # Verificação da eficiência
    print("\n🎯 ANÁLISE DE EFICIÊNCIA")
    print("=" * 80)
    # Aproximação para árvore AVL
    expected_height = int(1.44 * math.log2(5000 + 2) - 0.328)
    print(f"🔬 Altura máxima(pior caso): {expected_height}")
    print(f"🏗️  Altura real: {banking_system.get_tree_height()}")
    print(
        f"✅ Árvore está balanceada: {banking_system.get_tree_height() <= 2 * expected_height}"
    )


if __name__ == "__main__":
    main()
