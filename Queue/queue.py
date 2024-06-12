class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from an empty queue")
        return self.items.pop(0)

    def front(self):
        if self.is_empty():
            raise IndexError("Front from an empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Example Usage
if __name__ == "__main__":
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print("Queue after enqueuing 1, 2, 3:", queue)

    print("Front element is:", queue.front())

    queue.dequeue()
    print("Queue after dequeuing an element:", queue)

    print("Is queue empty?", queue.is_empty())

    queue.dequeue()
    queue.dequeue()
    print("Queue after dequeuing all elements:", queue)

    print("Is queue empty now?", queue.is_empty())
