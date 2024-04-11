class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def InsertTail(head, data):
    if head == None: return Node(data)
    head.next = InsertTail(head.next, data)
    return head

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

def MergeListsNope(headA, headB, merge=None):
    if headA == None and headB == None: return merge
    if headA == None:
        merge.next = headB
        return merge
    if headB == None:
        merge.next = headA
        return merge
    if headA.data < headB.data: return MergeLists(headA.next, headB, Node(headA.data, merge))
    return MergeLists(headA, headB.next, Node(headB.data, merge))

def nxtObj(a,b):
    if a.data < b.data: return a.next
    return a

def MergeLists(headA, headB):
    if headA == None: return headB
    if headB == None: return headA
    if headA.data < headB.data: return Node(headA.data, MergeLists(headA.next, headB))
    return Node(headB.data, MergeLists(headA, headB.next))

def GetNode(head, position, data=None):
    if head == None: return data if data == None else data[position]
    data = [head.data] + ([data] if data == None else data)
    return GetNode(head.next, position, data)

def test(sll):
    z = sll
    while not z.next == None:
        print(z.data)
        z = z.next
    print(z.data)
    return
