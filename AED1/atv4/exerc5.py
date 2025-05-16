class Node:
    def __init__(self, key=None):
        self.key = key
        self.prev = None
        self.next = None

class DoubleLinkedList:
    head = Node()
    size = 0

    def __init__(self, *values):
        self.head = None
        self.size = 0
        for value in values:
            self.add_tail(value)

    def add_head(self, key):
        temp = Node(key)
        if self.head is None:
            self.head = temp
            temp.next = None
        else:
            temp.next = self.head
            self.head.prev = temp
            self.head = temp
        temp.prev = None
        self.size += 1
    
    def add_tail(self, key):
        tail = Node(key)
        if self.head is None:
            self.head = tail
            tail.prev = None
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = tail
            tail.prev = temp
        tail.next = None
        self.size += 1
    
    def remove(self, key):
        current = self.head
        while current is not None:
            if current.key == key:
                break
            else:
                current = current.next
        if current is None:
            return False
        elif current is self.head:
            self.head = current.next
            self.head.prev = None
        else:
            current.prev.next = current.next
            current.next.prev = current.prev
        current.next = None
        current.prev = None
        self.size -= 1

    def __str__(self):
        result = []
        temp = self.head
        while temp is not None:
            result.append(str(temp.key))
            temp = temp.next
        return " -> ".join(result)

def pcritico(list):
    pcritico = 0
    if list.head is None or list.head.next is None or list.head.next.next is None:
        return pcritico

    current = list.head.next

    while current.next is not None:
        if current.key < current.prev.key and current.key < current.next.key:
            pcritico += 1
        elif current.key > current.prev.key and current.key > current.next.key:
            pcritico += 1
        current = current.next
    return pcritico

lista = DoubleLinkedList(1, 2, 3, 2, 1, 3, 2)
print(f"Numeros de pontos criticos: {pcritico(lista)}")

