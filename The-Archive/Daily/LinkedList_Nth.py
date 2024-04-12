class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def InsertNth(head, data, position):
    if not position: return Node(data, head)
    head.next = InsertNth(head.next, data, position-1)
    return head
