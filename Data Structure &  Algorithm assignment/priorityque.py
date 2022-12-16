# priorityque.py

from node import Node
from queue import Queue
from comparable import Comparable


class PriorityQueue(Queue):
    """A link-based priority queue implementation."""

    def __init__(self):
        self._head = None
        self._next = None
        self._size = 0

    def enqueue(self, new_item):
        """Inserts new_item after items of greater or equal
        priority or a__head of items of lesser priority.
        A has greater priority than B if A < B."""
        newNode = Node(new_item)
        if self._size == 0:
            self._head = newNode
            self._tail = newNode

        elif new_item == self._head._value:
            newNode._next = self._head._next
            self._head._next = newNode
        elif self._head._value < new_item:
            newNode._next = self._head
            self._head = newNode
        elif self._tail._value > new_item:
            temp = self._tail
            temp._next = newNode
            self._tail = newNode
        else:
            # Search for a position where it’s less
            temp = self._head
            while new_item <= temp._value:
                trail_node = temp
                temp = temp._next

            if new_item == temp._value:
                newNode._next = temp._next
                temp._next = newNode
            else:
                trail_node._next = newNode
                newNode._next = temp
        self._size += 1

    def dequeue(self):
        if self._head is None:
            raise IndexError("Can't dequeue! Queue is Empty")
        remove = self._head
        self._head = remove._next
        self._size -= 1
        return remove._value.data

    def peek(self):
        if self._head is None:
            raise Exception("Queue is Empty.")
        return self._tail._value.data

    def __contains__(self, data):
        temp = self._head
        while temp is not None:
            if temp._value.data == data:
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

    def __str__(self):
        temp = self._head
        out = ''
        while temp is not None:
            out += str(temp._value.data) + '<--'
            temp = temp._next
        return out[:-3]


if __name__ == "__main__":
    priorQue = PriorityQueue()
    # i = 10
    # for x in range(1, 3):
    #     priorQue.enqueue(Comparable(x, i))
    #     i -= 1
    # print(priorQue)
    # print(f"highest prority element removed: {priorQue.dequeue()}")
    priorQue.enqueue(Comparable(20, 0))
    print(priorQue)
    priorQue.enqueue(Comparable(220, 120))
    priorQue.enqueue(Comparable(120, 220))
    priorQue.enqueue(Comparable(240, 120))
    priorQue.enqueue(Comparable(0, 1000))
    print(priorQue)
    print(priorQue.contains(290))
    # priorQue.reverse()
    print(priorQue)
    print(len(priorQue))
    priorQue.dequeue()
    print(len(priorQue))
    print(priorQue)
