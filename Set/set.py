class MySet:
    def __init__(self, bucket_size=10):
        self.bucket_size = bucket_size
        self.buckets = [[] for _ in range(bucket_size)]
    
    def _hash(self, element):
        return hash(element) % self.bucket_size
    
    def add(self, element):
        bucket_index = self._hash(element)
        bucket = self.buckets[bucket_index]
        if element not in bucket:
            bucket.append(element)
    
    def remove(self, element):
        bucket_index = self._hash(element)
        bucket = self.buckets[bucket_index]
        if element in bucket:
            bucket.remove(element)
        else:
            raise KeyError(f"{element} not found in set")
    
    def contains(self, element):
        bucket_index = self._hash(element)
        bucket = self.buckets[bucket_index]
        return element in bucket
    
    def __iter__(self):
        for bucket in self.buckets:
            for element in bucket:
                yield element
    
    def __len__(self):
        return sum(len(bucket) for bucket in self.buckets)
    
    def __str__(self):
        elements = [element for bucket in self.buckets for element in bucket]
        return f"MySet({elements})"

# Usage example
my_set = MySet()

# Adding elements
my_set.add("apple")
my_set.add("banana")
my_set.add("cherry")
my_set.add("apple")  # Duplicate, will not be added

# Removing an element
my_set.remove("banana")

# Checking for membership
print(my_set.contains("apple"))  # Output: True
print(my_set.contains("banana"))  # Output: False

# Iterating over elements
for item in my_set:
    print(item)

# Getting the size of the set
print(len(my_set))  # Output: 2

# String representation of the set
print(my_set)  # Output: MySet(['apple', 'cherry'])
