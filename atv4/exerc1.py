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
    
## Função para inverter a lista

def InvertList(list):
    temp = list.head
    new_list = Linked_list()
    while temp is not None:
        new_list.add_head(temp.data)
        temp = temp.next
    return new_list

listinha = Linked_list(7, 12, 3, 29, 42, 10, 1, 5, 19, 4)
listinha = InvertList(listinha)
print(listinha)