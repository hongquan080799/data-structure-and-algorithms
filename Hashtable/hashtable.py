class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                kvp[1] = value
                return
        self.table[index].append([key, value])

    def lookup(self, key):
        index = self._hash(key)
        for kvp in self.table[index]:
            if kvp[0] == key:
                return kvp[1]
        return None

    def delete(self, key):
        index = self._hash(key)
        for i, kvp in enumerate(self.table[index]):
            if kvp[0] == key:
                del self.table[index][i]
                return

    def __str__(self):
        return str(self.table)

# Example Usage
if __name__ == "__main__":
    hashtable = HashTable()

    # Insert some key-value pairs
    hashtable.insert("apple", 1)
    hashtable.insert("banana", 2)
    hashtable.insert("orange", 3)
    print("Hashtable after inserting some elements:", hashtable)

    # Lookup a value
    print("Value for key 'banana':", hashtable.lookup("banana"))

    # Delete a key
    hashtable.delete("banana")
    print("Hashtable after deleting key 'banana':", hashtable)

    # Lookup a value for a deleted key
    print("Value for key 'banana':", hashtable.lookup("banana"))
