from linked_list import LinkedList


class HashTable:
    _data = None
    _CHAINING = True

    def __init__(self, size, chaining = True):
        self._CHAINING = chaining
        
        if self._CHAINING:
            self._data = []
            for i in range(size):
                self._data.append(LinkedList())
        else:
            self._data = [None]*size


    def _hash(self, key, increment = 0):
        return hash(key) + increment

    def _find_chaining(self, key):
        index = self._hash(key) % len(self._data)

        for i in self._data[index]:
            if i[0] == key:
                return i
        return None

    def __setitem__(self, key, value):
        index = self._hash(key) % len(self._data)

        if self._CHAINING:
            item = self._find_chaining(key)

            if item == None:
                self._data[index].add_first((key, value))       # insert
            else:
                self._data[index][self._data[index].find(item)] = (key, value)    # update
        else:
            i = 0
            while i < len(self._data):
                if self._data[index] is not None and self._data[index][0] != key:
                        index = self._hash(key, i) % len(self._data)
                        i += 1
                else:
                    self._data[index] = (key, value)        # insert and update
                    break
            if i == len(self._data):
                raise MemoryError("HashTable is Full")

    def __getitem__(self, key):
        index = self._hash(key) % len(self._data)

        if self._CHAINING:
            item = self._find_chaining(key)
            if item is None:
                raise ValueError("key doesn't exist")
            else:
                return item[1]
        else:

            i = 0
            while i < len(self._data):
                if self._data[index] is not None and self._data[index][0] != key:
                    index = self._hash(key, i) % len(self._data)
                    i += 1
                elif self._data[index] is None:
                    raise ValueError("key doesn't exist")
                else:
                    return self._data[index][1]

        return ValueError()

    def __contains__(self, key):
        index = self._hash(key) % len(self._data)

        if self._CHAINING:
            item = self._find_chaining(key)
            if item is not None:
                return True
        else:
            i = 0
            while i < len(self._data):
                if self._data[index] is not None and self._data[index][0] != key:
                    index = self._hash(key, i) % len(self._data)
                    i += 1
                elif self._data[index] is not None:
                    return True
                else:
                    break
        return False

    def __delitem__(self, key):
        if self._CHAINING:

            item = self._find_chaining(key)
            if item is not None:
                index = self._hash(key) % len(self._data)
                self._data[index].remove_at(self._data[index].find(item))
            else:
                raise ValueError("Key doesn't exist")

        else:
            raise NotImplementedError("Can't delete using open addressing")