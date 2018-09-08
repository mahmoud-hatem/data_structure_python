from linked_list import LinkedList


def main():
    l = LinkedList()
    l.add_first(1)
    l.add_last(4)

    l.add_at(2, 1)
    l.add_at(3, 2)

#   test add_at()
#    l.add_at(10, 9)
#    l.add_at(-1, -2)

    print(l)

    print(l.remove_first())
    print(l.remove_last())
    print(l)
    l.add_last(5)
    l.add_last(6)
    print(l)
    print(l.remove_at(1))
    print(l)
    print(l.find(5))

    print(len(l))

    for i in range(1000000):
        l.add_last(i)
    l.clear()

    x = 0

if __name__ == '__main__':
    main()