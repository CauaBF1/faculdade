class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
    

class Linked_list_Order:
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
            else:
                if temp.data > value:
                    break
                else:
                    temp = temp.next
        return False
    
    def add(self, value):
        current = self.head
        previous = None

        while current is not None:
            if current.data > value:
                break
            else:
                previous = current
                current = current.next
        
        temp = Node(value)
        if previous is None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = current
            previous.next = temp
    
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
    merged_list = Linked_list_Order()
    current1 = list1.head
    current2 = list2.head

    while current1 is not None:
        merged_list.add(current1.data)
        current1 = current1.next

    while current2 is not None:
        merged_list.add(current2.data)
        current2 = current2.next
    
    return merged_list
    
    
lista1 = Linked_list_Order(5, 12, 19, 23, 29, 42)
lista2 = Linked_list_Order(2, 3, 7, 15, 20, 25, 33, 39)
merged = merge(lista1, lista2)

print(merged)
