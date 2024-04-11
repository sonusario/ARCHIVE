#32 to and including 126
# 0 to and including  94
#' ' to '~'
#Mid is 79 ord
#Mid is 'O' chr
#Mid is 47 in arr
#Len is 95

def buildKey():
    alnu = {}
    for i in range(95):
        alnu[chr(i + 32)] = i
    return alnu

alphaNum = buildKey()

def b95toDec(num):
    numLen = len(num) - 1
    total = 0
    for c in num:
        total += (95**numLen) * alphaNum[c]
        numLen -= 1
    return total

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
