from linked_list import LinkedList


class Queue:
    _data = LinkedList()

    def enqueue(self, element):
        self._data.add_last(element)

    def dequeue(self):
        if self.is_empty():
            raise ValueError("queue is empty")

        return self._data.remove_first()

    def first(self):
        if self.is_empty():
            raise ValueError("queue is empty")

        return self._data[0]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._data)