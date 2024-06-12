class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Example Usage
if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print("Stack after pushing 1, 2, 3:", stack)

    print("Top element is:", stack.peek())

    stack.pop()
    print("Stack after popping an element:", stack)

    print("Is stack empty?", stack.is_empty())

    stack.pop()
    stack.pop()
    print("Stack after popping all elements:", stack)

    print("Is stack empty now?", stack.is_empty())
