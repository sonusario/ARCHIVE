class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Insert(head, data):
    if head == None: return Node(data)
    head.next = Insert(head.next, data)
    return head
