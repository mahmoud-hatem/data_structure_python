from linked_list import LinkedList


class Stack:
    _data = LinkedList()

    def push(self, element):
        self._data.add_last(element)

    def pop(self):
        if self.is_empty():
            raise ValueError("stack is empty")

        return self._data.remove_last()

    def top(self):
        if self.is_empty():
            raise ValueError("stack is empty")

        return self._data[len(self) - 1]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._data)