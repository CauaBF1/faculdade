class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    

class Linked_list:
    #Contrutor para adicionar varios de uma vez para facilitar o teste
    def __init__(self, *values):
        self.head = None
        self.size = 0
        for value in values:
            self.add_tail(value)

    def add_head(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp
        self.size += 1

    def add_tail(self, value):
        tail = Node(value)
        if self.head is None:
            self.head = tail
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = tail
        tail.next = None
        self.size += 1

    def length(self):
        return self.size
    
    def search(self, value):
        temp = self.head
        while temp is not None:
            if temp.data == value:
                return True
            temp = temp.next
        return False
    
    def remove(self, value):
        current =  self.head
        previsous = None

        while current is not None:
            if current.data == value:
                break
            else:
                previsous = current
                current = current.next
        if previsous == None:
            self.head = current.next
        else:
            previsous.next = current.next
        current.next = None
    # Função para printar a lista, para facilitar a visualização
    def __str__(self):
        result = []
        temp = self.head
        while temp is not None:
            result.append(str(temp.data))
            temp = temp.next
        return " -> ".join(result)

def merge(list1, list2):
    # Se uma lista estiver vazia, retorna a outra
    if list1.head is None:
        return list2
    if list2.head is None:
        return list1
    
    merged_list = Linked_list()
    temp1 = list1.head
    temp2 = list2.head

    while temp1 and temp2:
        if temp1.data < temp2.data:
            merged_list.add_tail(temp1.data)
            temp1 = temp1.next
        else:
            merged_list.add_tail(temp2.data)
            temp2 = temp2.next

    while temp1:
        merged_list.add_tail(temp1.data)
        temp1 = temp1.next

    while temp2:
        merged_list.add_tail(temp2.data)
        temp2 = temp2.next
    
    return merged_list

lista1 = Linked_list(5, 12, 19, 23, 29, 42)
lista2 = Linked_list(2, 3, 7, 15, 20, 25, 33, 39)
merged = merge(lista1, lista2)

print(merged)
