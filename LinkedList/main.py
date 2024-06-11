class Node:
    def __init__(self, data):
        self.data = data
        self.next = None



def insert_at_beginning(head: Node,data):
    new_node = Node(data)
    new_node.next = head
    head = new_node

def insert_at_end(head: Node, data):
    new_node = Node(data)
    if head is None:
        head = new_node
        return
    last = head
    while last.next:
        last = last.next
    last.next = new_node

def insert_at_position(head: Node, data, position):
    if position < 0:
        raise ValueError("Position must be a non-negative integer.")
    new_node = Node(data)
    if position == 0:
        new_node.next = head
        head = new_node
        return
    current = head
    count = 0
    while current is not None and count < position - 1:
        current = current.next
        count += 1
    if current is None:
        raise IndexError("Position out of bounds.")
    new_node.next = current.next
    current.next = new_node

def print_list(head: Node):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
   

# Example Usage
if __name__ == "__main__":
   head = Node(1)
   insert_at_end(head, 2)
   insert_at_end(head, 3)
   insert_at_end(head, 4)
   print_list(head)
