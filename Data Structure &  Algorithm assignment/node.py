class Node:
    def __init__(self, _value, next_node=None):
        self._value = _value
        self._next = next_node

    def __str__(self):
        return str(self._value)


