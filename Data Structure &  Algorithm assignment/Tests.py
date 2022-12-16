import unittest
from Stack import Stack
from linkedList import LinkedList
from queue import Queue
from priorityque import PriorityQueue
from comparable import Comparable
from hastable import HashTable


class TestStack(unittest.TestCase):
    """ initializing the stack and adding 1,2,3,4,5,6,7,8,9,10 elements to the list so our stack is like 5,4,3,2,1
    so our top element will be 5 and bottom element will be 1 assuming this
    all test cases are witten"""

    stack = Stack()
    for i in range(1, 6):
        stack.push(i)

    def test_peek(self):
        # self.assertEqual(stack.contains(12), False)
        self.assertEqual(TestStack.stack.peek(), 5)

    def test_contain(self):
        self.assertTrue(2 in TestStack.stack, 'test case passed')

    def test_pop(self):
        self.assertEqual(TestStack.stack.pop(), 5)

    stack.push(5)  # pushing again the same element for further

    def test_size(self):
        self.assertEqual(len(TestStack.stack), 5)


class TestLinkedlist(unittest.TestCase):
    """ initializing a Linked list and adding 1,2,3,4,5,6,7,8,9,10 elements to the list assuming this
        all test cases are witten
        Last elemet: 10
        First elemrt: 1"""

    List = LinkedList()
    for x in range(11):  # Adding elements to the list
        List.insert(x)

    def test_insert(self):
        """Assuming that deletion is only possible if previously it was inserted"""
        self.assertEqual(TestLinkedlist.List.delete(), 10)
        self.assertEqual(TestLinkedlist.List.delete(), 9)
        TestLinkedlist.List.insert(9)
        TestLinkedlist.List.insert(10)

    def test_deleteAt(self):
        # At index 2 there is 3. hence 3 it should be deleted and returned to pass the case.
        self.assertEqual(TestLinkedlist.List.deleteAt(2), 3)

    def test_center(self):
        # the center element in our list is 5, 5 should be returned by the test function
        self.assertEqual(TestLinkedlist.List.centre(), 5)

    def test_size(self):
        # length of created linked list size is 10
        self.assertEqual(len(TestLinkedlist.List), 10)
        TestLinkedlist.List.delete()  # after deletion of an element size should be updated
        self.assertEqual(len(TestLinkedlist.List), 9)


class TestQueue(unittest.TestCase):
    """ Adding element 1,2,3,4,5,6,7,8,9,10 in the Queue where first element
    to come is 1 which will be first out as per the condition of FIFO"""

    que = Queue()  # Initialising the Que
    # Adding elements to the que
    for i in range(1, 11):
        que.enqueue(i)

    def test_deque(self):
        self.assertEqual(TestQueue.que.dequeue(), 1)

    def test_peek(self):
        self.assertEqual(TestQueue.que.peek(), 2)  # First element to move out from the Que will be 2.

    def test_contains(self):
        self.assertTrue(2 in TestQueue.que)  # 2 is in the que and it should return True.
        self.assertTrue(not 200 in TestQueue.que)  # 200 is not in the que, it should return False.

    def test_size(self):
        self.assertEqual(len(TestQueue.que), 9)  # After removing the element from the que size was reduced to 9.


class TestPriorityQueue(unittest.TestCase):
    """creating a priority queue and adding three elements Nilesh,
    Anoop, Rahul with priority 1,2,3 respectively in dequeue method
    high priority element Rahul should pop irrespective of the time
    it came. Let's  check this! Priority Queue is derived from Queue therefore
    all functions are already been working we will check only this enqueue
    property"""

    priorityQue = PriorityQueue()
    priorityQue.enqueue(Comparable('Anoop', 2))
    priorityQue.enqueue(Comparable('Nilesh', 1))
    priorityQue.enqueue(Comparable('Rahul', 3))

    def test_dequeue(self):
        self.assertEqual(TestPriorityQueue.priorityQue.dequeue(), 'Rahul')


class TestHashTable(unittest.TestCase):

    def test_hashing_function(self):
        key = 9
        SIZE = 100
        hash_key = key % SIZE
        self.assertAlmostEqual(HashTable.hashing(SIZE,key), hash_key)


if __name__ == "__main__":
    unittest.main()
