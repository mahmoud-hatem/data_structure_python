from builtins import print

from hash_table import HashTable
from linked_list import LinkedList
from queue import Queue
from stack import Stack


def test_list():
    l = LinkedList()
    l.add_first(1)
    l.add_last(4)

    l.add_at(2, 1)
    l.add_at(3, 2)
    for i in l:
        print("hi" + str(i))

    #   test add_at()
    #    l.add_at(10, 9)
    #    l.add_at(-1, -2)

    # print(l)
    #
    # print(l.remove_first())
    # print(l.remove_last())
    # print(l)
    # l.add_last(5)
    # l.add_last(6)
    # print(l)
    # print(l.remove_at(1))
    # print(l)
    # print(l.find(5))
    #
    # print(len(l))
    # print(l[0])
    # l[0] = 9
    # print(l)
    #
    # # for i in range(1000000):
    # #     l.add_last(i)
    # # l.clear()
    #
    # l2 = LinkedList()
    # l2.add_last(1)
    # l2.add_last(3)
    # l2.add_last(4)
    #
    # print(l2)

def test_stack():
    s = Stack()

    for i in range(5):
        s.push(i)

    print(s.top())

    while s.is_empty() == False:
        print(s.pop(), end=" ")

    # s.top()

def test_queue():
    q = Queue()
    for i in range(5):
        q.enqueue(i)

    print(q.first())

    while not q.is_empty():
        print(q.dequeue(), end=" ")

def test_hash_table():
    size = 28
    h = HashTable(size)
    for i in range(ord('a'), ord('z')):
        h[chr(i)] = i - ord('a')

    print(h['x'])
    h['x'] = 5
    print(h['x'])

    del h['x']


    y = 0


def main():
    # test_list()
    # test_stack()
    # test_queue()
    test_hash_table()
    x = 0

if __name__ == '__main__':
    main()