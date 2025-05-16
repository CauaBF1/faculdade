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

def pcritico(list):
    pcritico = 0
    if list.head is None or list.head.next is None or list.head.next.next is None:
        return pcritico

    current = list.head.next
    previous = list.head
    following = list.head.next.next

    while following is not None:
        if current.data < previous.data and current.data < following.data:
            pcritico += 1
        elif current.data > previous.data and current.data > following.data:
            pcritico += 1
        previous = current
        current = following
        following = following.next
    return pcritico

lista = Linked_list(1, 2, 3, 2, 1, 3, 2)
print(f"Numeros de pontos criticos: {pcritico(lista)}")