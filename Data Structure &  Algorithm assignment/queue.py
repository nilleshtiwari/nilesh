#  Implementation of Que using List inbuilt Data Structures.
from node import Node


class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, data):
        node = Node(data)
        if self._head is None:
            self._head = self._tail = node
            self._size += 1
        else:
            last = self._tail
            last._next = node
            self._tail = node
            self._size += 1

    def dequeue(self):
        if self._head is None:
            raise IndexError("Can't dequeue! Queue is Empty")
        remove = self._head
        self._head = remove._next
        self._size -= 1
        return remove._value

    def peek(self):
        if self._head is None:
            raise Exception("Queue is Empty.")
        return self._head._value

    def __contains__(self, data):
        temp = self._head
        while temp is not None:
            if temp._value == data:
                return True
            temp = temp._next
        return False

    def __len__(self):
        return self._size

    def reverse(self):
        self._tail = self._head
        prev = None
        current = self._head
        while current is not None:
            _nextNode = current._next
            current._next = prev
            prev = current
            current = _nextNode
        self._head = prev

    def __iter__(self):
        current = self._head
        while current is not None:
            yield current
            current = current._next

    def __str__(self):
        temp = self._head
        out = ''
        while temp is not None:
            out += str(temp._value) + "<--"
            temp = temp._next
        return out[:-3]


if __name__ == "__main__":
    que = Queue()
    for i in range(1, 11):
        que.enqueue(i)
    print(que)
    que.dequeue()

    #que.reverse()
    print(que)
    for x in que:
        print(x)
    print(len(que))

    print(que.contains(20))
    print(f"peek element : {que.peek()}")