#  Generic implementation of Stack using Node
from node import Node


class Stack:

    # Initializing a stack.
    # Using dummy node to handle edge cases easily
    def __init__(self):
        self._head = Node("_head")
        self._size = 0
        self.current_node = 0

    # Push a _value into the stack.
    def push(self, _value):
        node = Node(_value)
        node._next = self._head._next
        self._head._next = node
        self._size += 1

    # Remove a _value from the stack and return.
    def pop(self):
        if self._size == 0:
            raise Exception("Popping from an empty stack")
        remove = self._head._next
        self._head._next = self._head._next._next
        self._size -= 1
        return remove._value

    # To get the top item of the stack
    def peek(self):
        if self._size == 0:  # Checking to see whether stack is empty or not first
            raise Exception("Peeking from an empty stack")
        return self._head._next._value

    def __contains__(self, val):
        current = self._head._next
        while current is not None:
            if current._value == val:
                return True
            current = current._next
        return False

    # To get the current _size of the stack
    def __len__(self):
        return self._size

    def reverse(self):
        prev = None
        current = self._head._next
        while current is not None:
            _next = current._next
            current._next = prev
            prev = current
            current = _next
        self._head._next = prev

    #  implementing iterator
    def __iter__(self):
        current = self._head._next
        while current is not None:
            yield current
            current = current._next

    # String representation of the stack
    def __str__(self):
        current_node = self._head._next  # to get the top element in the stack which is referenced by dummy node
        output_string = ""
        while current_node is not None:
            output_string += str(current_node._value) + "->"
            current_node = current_node._next
        return output_string[:-2]


#Driver Code
if __name__ == "__main__":
    stack = Stack()
    for i in range(1, 11):
        stack.push(i)
    print(f"Stack: {stack}")
    print(stack.peek())
    print(f"removed element: {stack.pop()}")
    print(stack)

    for _ in range(1, 6):
        remove = stack.pop()
        print(f"Pop: {remove}")
    print(f"Stack: {stack}")
    #
    # print(stack.contains(12))

#  Time complexity is O(1) for all the operations such as peek push pop.
#
# for x in iter(stack):
#     print(x)
# print(stack)
# stack.reverse()
# print(f"_size after reverse: {stack._size}")
# for x in iter(stack):
#     print(x)
# print(stack)
# print(stack.contains(12))
# print(f"removed element: {stack.pop()}")
#
# print(f"_size of stack: {stack._size}")
# print(len(stack))
