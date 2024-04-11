class Zode():
    def __init__(self, data=None, next_node=None, prev_node=None):
        self.data = data
        self.next = next_node
        self.prev = prev_node

class Node():
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

def InsertTail(head, data):
    if head == None: return Node(data)
    head.next = InsertTail(head.next, data)
    return head

def InsertTail_DLL(head, data, naxt=None, prev=None):
    if head == None: return Zode(data)
    head.next = InsertTail_DLL(head.next, data, None, head)
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

def RemoveDuplicates(head, prev=None):
    if head == None: return head
    if prev == None: head.next = RemoveDuplicates(head.next, head)
    elif prev.data == head.data: head = RemoveDuplicates(head.next, prev)
    else: head.next = RemoveDuplicates(head.next, head)
    return head

'''
def has_cycle(head, visited=[]):
    if head == None: return False
    if head in visited: return True
    return has_cycle(head.next, visited + [head])
'''

def has_cycle(head, pHead=None):
    if head == None: return False
    if pHead == None: pHead = head
    if head.next == pHead: return True
    return has_cycle(head.next, pHead)

def has_cycleL(head):
    pHead = head
    head = head.next
    while head:
        if pHead == head: return True
        head = head.next
    return False

'''
def FindMergeNode(headA, headB):
    while headA:
        headA.data = [headA.data]
        headA = headA.next
    while headB:
        if type(headB.data) == type([]): return headB.data[0]
        headB = headB.next


def FindMergeNode(headA, headB):
    x = None
    hA = headA
    while headA:
        headA.data = [headA.data]
        headA = headA.next
    while headB:
        if type(headB.data) == type([]):
            x = headB.data[0]
            break
        headB = headB.next
    while hA:
        hA.data = hA.data[0]
        hA = hA.next
    return x
'''

def FindMergeNode(headA, headB):
    while headA:
        headA.data = [headA.data]
        headA = headA.next
    while headB:
        if type(headB.data) == type([]):
            x = headB.data[0]
            while headB:
                headB.data = headB.data[0]
                headB = headB.next
            return x
        headB = headB.next

'''
def SortedInsert(head, data): #dll
    oHead = head
    while head:
        if data <= head.data:
            head = Zode(data, head, head.prev)
            while head.prev:
                head = head.prev
            return head
        if head.next == None:
            head.next = Zode(data, None, head)
            return oHead
        head = head.next
        
    return Zode(data, None, None)
'''

def rollback(head):
    while head.prev:
        head = head.prev
    return head

def SortedInsert(head, data):
    if head == None: return Zode(data)
    if data <= head.data:
        prv = head.prev
        head = Zode(data, head, head.prev)
        head.next.prev = head
    else:
        while head.next:
            if data <= head.next.data:
                prv = head.next.prev
                head.next = Zode(data, head.next, head)
                head.next.next.prev = head.next
                return rollback(head)
            head = head.next
        head.next = Zode(data, None, head)
        head = rollback(head)
    return head

def SortedInsert2(head,data):
    if head == None: return Zode(data, None, head)
    if data <= head.data:
        prv = head.prev
        head = Zode(data, head, head.prev)
        head.next.prev = head
        return head
    head.next = SortedInsert2(head.next, data)
    return head

'''
def rev(p, q=None):
    if p == None: return q
    return rev(p.next, Node(p.data,q))
'''

def ReverseDLL(head, q=None):
    if head == None: return q
    return ReverseDLL(head.next, Zode(head.data,q,head))

def ReverseDLL2(head):
    oh = None
    while head:
        h = head.next
        head.next = head.prev
        head.prev = h
        oh = head
        head = head.prev
    return oh

def ReverseDLL3(head):
    newFirst = None
    while head:
        head.next, head.prev = head.prev, head.next
        newFirst = head
        head = head.prev
    return newFirst

def test(sll):
    z = sll
    while not z.next == None:
        print(z.data)
        z = z.next
    print(z.data)
    return
