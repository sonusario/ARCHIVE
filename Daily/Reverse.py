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

def ReversePrint(head):
    if head == None: return
    ReversePrint(head.next)
    print(head.data)
    return

def revCore(head,nxt):
    if head.next == None:
        head.next = nxt
        return head
    txn = head.next
    head.next = nxt
    return revCore(txn,head)

def Reverse(head):
    if head == None: return
    if head.next == None: return head
    txn = head.next
    head.next = None
    return revCore(txn, head)

def rc(current, prev, nxt):
    if current == None: return prev
    nxt = current.next
    current.next = prev
    return rc(nxt, current, nxt)

def Rev(head):
    return rc(head, None, None)

def qa(current, prev=None, nxt=None):
    if current == None: return prev
    nxt = current.next
    current.next = prev
    return qa(nxt, current, nxt)

def aq(head, sll=None):
    if head == None: return sll
    nxt = head.next
    head.nxt = sll
    return aq(nxt, head)

def rev(p, q=None):
    if p == None: return q
    return rev(p.next, Node(p.data,q))

def compare(headA, headB):
    if headA == None or headB == None: return int(headA == headB)
    if not(headA.data == headB.data): return 0
    return compare(headA.next, headB.next)

def MergeLists(headA, headB):
    if headA == None: return headB
    if headB == None: return headA
    

def test(sll):
    z = sll
    while not z.next == None:
        print(z.data)
        z = z.next
    print(z.data)
    return
