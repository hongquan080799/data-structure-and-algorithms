class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def insert_at_end(head: Node, data):
    new_node = Node(data)
    if head is None:
        head = new_node
        return
    last = head
    while last.next:
        last = last.next
    last.next = new_node

def search(head: Node, key):
    current = head
    position = 0
    while current:
        if current.data == key:
            return position
        current = current.next
        position += 1
    return -1

if __name__ == "__main__":
    head = Node(1)
    insert_at_end(head, 2)
    insert_at_end(head, 3)
    insert_at_end(head, 4)

    print(search(head, 2))