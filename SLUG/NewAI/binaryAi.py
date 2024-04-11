def bio(b,i,o):
    return (b**o) ** (b**i)

class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def Delete(head, position):
    if not position: return head.next
    head.next = Delete(head.next, position-1)
    return head

def InsertNth(head, data, position):
    if not position: return Node(data, head)
    head.next = InsertNth(head.next, data, position-1)
    return head

def test(sll):
    z = sll
    while not z.next == None:
        print(z.data)
        z = z.next
    print(z.data)
    return
