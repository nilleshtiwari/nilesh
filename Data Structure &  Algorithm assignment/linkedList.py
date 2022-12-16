from node import Node


class LinkedList:
    def __init__(self, _values=None):
        self._head = None
        self._tail = None
        self._size = 0

    def insert(self, data):  # this method will insert data node at the end.
        new_node = Node(data)
        if self._head is None:
            self._head = new_node
            self._tail = new_node
            self._size += 1
        else:
            self._tail._next = new_node
            self._tail = new_node
            self._size += 1
            return self._tail

    def insertAt(self, index, data):
        new_node = Node(data)
        if index > self._size:
            raise IndexError("Index out of range")
        elif index == 0:
            new_node._next = self._head
            self._head = new_node
            if self._size == 0: self._tail = new_node
            self._size += 1
            return self._head
        else:
            temp = self._head
            i = 1
            while i < index:
                temp = temp._next
                i += 1
            new_node._next = temp._next
            temp._next = new_node
            self._size += 1
            return new_node

    def delete(self):
        temp = self._head
        n = self._size
        while n > 2:
            temp = temp._next
            n -= 1
        remove = temp._next
        temp._next = None
        self._tail = temp
        self._size -= 1
        return remove._value


    def deleteAt(self, index):
        if index > self._size:
            raise IndexError("Index out of range")
        temp = self._head
        while index >= 0:
            prev = temp
            temp = temp._next
            index -= 1
        prev._next = temp._next
        self._size -= 1
        return temp._value

    def centre(self):
        middle = self._size // 2
        temp = self._head
        while middle > 0:
            temp = temp._next
            middle -= 1
        return temp._value

    def reverse(self):
        self._tail = self._head
        prev = None
        current = self._head
        while current is not None:
            _next = current._next
            current._next = prev
            prev = current
            current = _next
        self._head = prev

    def __len__(self):
        return self._size

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current
            current = current._next

    def __str__(self):
        curr = self._head
        out = ''
        while curr is not None:
            out += str(curr._value) + '-->'
            curr = curr._next
        return out[:-3]


if __name__ == "__main__":

    List = LinkedList()

    for x in range(11):
        List.insert(x)
    print(List)
    
    print(f"deleted element: {List.delete()}")
    print(f"deleted element: {List.delete()}")


