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
def delete_from_beginning(head: Node):
    if head is None:
        raise IndexError("List is empty.")
    head = head.next

def delete_from_end(head: Node):
    if head is None:
        raise IndexError("List is empty.")
    if head.next is None:
        head = None
        return
    second_last = head
    while second_last.next.next:
        second_last = second_last.next
    second_last.next = None

def delete_from_position(head: Node, position):
    if head is None:
        raise IndexError("List is empty.")
    if position < 0:
        raise ValueError("Position must be a non-negative integer.")
    if position == 0:
        head = head.next
        return
    current = head
    count = 0
    while current is not None and count < position - 1:
        current = current.next
        count += 1
    if current is None or current.next is None:
        raise IndexError("Position out of bounds.")
    current.next = current.next.next

def print_list(head: Node):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")
if __name__ == "__main__":
    head = Node(1)
    insert_at_end(head, 2)
    insert_at_end(head, 3)
    insert_at_end(head, 4)



    # delete from the end
    delete_from_end(head)
    print_list(head)