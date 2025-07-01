class HashTableLinearProbing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.collisions = 0

    def _hash1(self, key):
        return key % self.size

    def insert(self, key):
        initial_index = self._hash1(key)
        index = initial_index
        
        # Procura próxima posição disponível em caso de colisão (linear probing)
        while self.table[index] is not None:
            self.collisions += 1
            index = (index + 1) % self.size
            if index == initial_index:  # Tabela está cheia
                print(f"Erro: Tabela hash cheia. Não foi possível inserir {key}")
                return
        self.table[index] = key

    def display(self):
        print("Tabela Hash (Sondagem Linear):")
        for i, value in enumerate(self.table):
            print(f"[{i}] -> {value}")
        print(f"Total de colisões: {self.collisions}")

class HashTableDoubleHashing:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size
        self.collisions = 0

    def _hash1(self, key):
        return key % self.size

    def _hash2(self, key):
        # Garante que size-1 não seja zero para o módulo
        return 1 + (key % (self.size - 1)) if self.size > 1 else 1

    def insert(self, key):
        initial_index = self._hash1(key)
        index = initial_index
        i = 0
        
        # Procura próxima posição disponível usando double hashing
        while self.table[index] is not None:
            self.collisions += 1
            i += 1
            index = (self._hash1(key) + i * self._hash2(key)) % self.size
            # Previne loop infinito se a tabela estiver cheia ou a função de hash for inadequada
            if i > self.size:
                print(f"Erro: Tabela hash cheia ou não foi possível inserir {key}")
                return
        self.table[index] = key

    def display(self):
        print("Tabela Hash (Double Hashing):")
        for i, value in enumerate(self.table):
            print(f"[{i}] -> {value}")
        print(f"Total de colisões: {self.collisions}")

# Execução principal — Questão 3 - Parte A
if __name__ == "__main__":
    keys_part_a = [25, 47, 98, 13, 52, 75, 67, 32, 81, 11, 89, 55, 29, 39, 42]
    table_size_part_a = 17

    print("--- Questão 3 - Parte A: Sondagem Linear ---")
    hash_table_lp = HashTableLinearProbing(table_size_part_a)
    for key in keys_part_a:
        hash_table_lp.insert(key)
    hash_table_lp.display()

    # Questão 3 - Parte B: Double Hashing
    print("\n--- Questão 3 - Parte B: Double Hashing ---")
    # Para double hashing, h2(k) = 1 + (k mod 13). Então, M deve ser > 13. M=17 está adequado.
    hash_table_dh = HashTableDoubleHashing(table_size_part_a)
    for key in keys_part_a:
        hash_table_dh.insert(key)
    hash_table_dh.display()

    # Questão 3 - Parte C: Redimensionamento Dinâmico
    print("\n--- Questão 3 - Parte C: Redimensionamento Dinâmico ---")
    # Utilizando a tabela linear probing já populada para o exemplo de redimensionamento
    
    current_keys = [key for key in hash_table_lp.table if key is not None]
    current_num_elements = len(current_keys)
    current_load_factor = current_num_elements / hash_table_lp.size

    print(f"Tamanho inicial da tabela: {hash_table_lp.size}")
    print(f"Número de elementos atuais: {current_num_elements}")
    print(f"Fator de carga atual: {current_load_factor:.2f}")

    if current_load_factor > 0.7:
        new_size = 37  # M' = 37 como especificado
        print(f"Fator de carga > 0.7. Redimensionando para o novo tamanho: {new_size}")
        
        resized_hash_table_lp = HashTableLinearProbing(new_size)
        print("Reinserindo chaves existentes...")
        for key in current_keys:
            resized_hash_table_lp.insert(key)
        
        new_keys_to_insert = [12, 23, 66, 91, 44, 56, 78, 99]
        print(f"Inserindo novas chaves: {new_keys_to_insert}")
        for key in new_keys_to_insert:
            resized_hash_table_lp.insert(key)
        
        resized_hash_table_lp.display()
    else:
        print("Fator de carga não ultrapassou 70%. Não será necessário redimensionar neste exemplo.")
