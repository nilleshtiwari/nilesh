# hashtable.py

class HashTable:

    def __init__(self, size=100):
        self._size = size
        self._hash_table = [[] for _ in range(self._size)]

    def insert(self, key, value):
        size = self._size
        hash_key = HashTable.hashing(size, key)
        while len(self._hash_table[hash_key]) != 0:
            hash_key += 1
            if hash_key >= self.size:
                raise Exception("Cannot insert Hash Table completely filled!")
        self._hash_table[hash_key].append(value)

    @staticmethod
    def hashing(size, key):
        return key % size

    def delete(self, key):
        hash_key = HashTable.hashing(self._size, key)
        self._hash_table[hash_key] = []

    def __contains__(self, key):
        if key in self._hash_table:
            return True
        return False

    def get_value_by_key(self, key):
        hash_key = HashTable.hashing(self._size, key)
        return self._hash_table[hash_key]

    def __len__(self):
        return self._size

    def __iter__(self):
        for x in self._hash_table:
            yield x

    def __str__(self):
        output = ''
        for i in range(self.size):
            if len(self._hash_table[i]) != 0:
                output += str(i)
                for j in self._hash_table[i]:
                    output += '-->' + str(j)
                output += '\n'

        return output


if __name__ == '__main__':
    HashTable = HashTable()
    HashTable.insert(10,'allahabad')
    HashTable.insert(25, 'Mumbai')
    HashTable.insert(20,'mathura')
    HashTable.insert(9,'delhi')
    HashTable.insert(21,'Punjab')
    print(HashTable)
