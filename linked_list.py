class LinkedList:
    _head = None
    _tail = None
    _size = 0

    ########################## Node ############################
    class _Node:
        element = None
        next = None

        def __init__(self, element, next = None):
            self.element = element
            self.next = next

    ######################## End Node ##########################

    def add_first(self, element):
        new_node = LinkedList._Node(element)

        if self._head == None:
            self._head = self._tail = new_node
        else:
            new_node.next = self._head
            self._head = new_node

        self._size += 1

    def add_last(self, element):
        new_node = LinkedList._Node(element)

        if self._tail == None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

        self._size += 1

    def add_at(self, element, index):

        if index < 0 or self._size < index:
            raise ValueError("invalid index")

        if index == 0:
            self.add_first(element)
        elif index == self._size:
            self.add_last(element)
        else:
            new_node = LinkedList._Node(element)

            node_before_index = self._get_node_at(index - 1)
            new_node.next = node_before_index.next
            node_before_index.next = new_node

            self._size += 1

    def remove_first(self):
        removed_node = self._head
        self._head = self._head.next

        self._size -= 1

        return removed_node.element

    def remove_last(self):
        removed_node = self._tail

        node_before_tail = self._get_node_at(self._size - 2)   # get the node before tail
        node_before_tail.next = None
        self._tail = node_before_tail

        self._size -= 1

        return removed_node.element

    def remove_at(self, index):
        if index < 0 or self._size <= index:
            raise ValueError("invalid index")

        if index == 0:
            return self.remove_first()
        elif index == self._size - 1:
            return self.remove_last()
        else:
            node_before_index = self._get_node_at(index - 1)
            removed_node = node_before_index.next

            node_before_index.next = removed_node.next

            self._size -= 1

            return removed_node.element

    # return index of element or -1 if not find
    def find(self, element):
        current_node = self._head

        for i in range(self._size):
            if current_node.element == element:
                return i
            current_node = current_node.next

        return -1

    def clear(self):
        self._head = self._tail = None
        self._size = 0

    # get node at index
    def _get_node_at(self, index):
        tmp = self._head
        for i in range(index):
            tmp = tmp.next

        return tmp

    def __str__(self):
        s = ""
        tmp = self._head
        for i in range(self._size):
            s += str(tmp.element) + " "
            tmp = tmp.next

        return s.rstrip()

    def __len__(self):
        return self._size

    def __getitem__(self, index):
        if index < 0 or self._size <= index:
            raise ValueError("invalid index")
        return self._get_node_at(index).element