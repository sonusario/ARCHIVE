class Node():
    def __init__(self, M, G, F, setters, left_node, right_node):
        self.M = M
        self.G = G
        self.F = F
        self.setters = setters
        self.left = left_node
        self.right = right_node

def Insert(head):
    if head.M == 9 and head.G == 14 and head.F == 15:
        print(head.M, head.G, head.F)
        return Node(head.M, head.G, head.F, head.setters, None, None)
    elif head.M > 9 and head.G > 14 and head.F > 15:
        return Node(head.M, head.G, head.F, head.setters, None, None)
    if head.setters == 'MG':
        head.left = Insert(Node(head.M+1,head.G,head.F+1,'MF',None,None))
        head.right = Insert(Node(head.M,head.G+1,head.F+1,'GF',None,None))
    elif head.setters == 'MF':
        head.left = Insert(Node(head.M+1,head.G+1,head.F,'MG',None,None))
        head.right = Insert(Node(head.M,head.G+1,head.F+1,'GF',None,None))
    elif head.setters == 'GF':
        head.left = Insert(Node(head.M+1,head.G,head.F+1,'MF',None,None))
        head.right = Insert(Node(head.M+1,head.G+1,head.F,'MG',None,None))
    return head

from random import randrange
from copy import deepcopy as cpy

def getPopMember():
    member = []
    last = None
    available = [0,1,2]
    for i in range(19):
        if last == None:
            last = randrange(3)
            del available[available.index(last)]
            member.append(last)
        else:
            available.append(last)
            last = available[randrange(2)]
            del available[available.index(last)]
            member.append(last)
    return member

def initPop(n):
    pop = []
    for i in range(n):
        pop.append(getPopMember())
    return pop

def gradePop(pop, gc):
    gradeFlag = False
    bestMember = 0
    scores = []

    bestScore = -100
    for i in range(len(pop)):
        m = 0
        g = 0
        f = 0
        for j in range(19):
            if pop[i][j] == 0:
                m += 1
                g += 1
            elif pop[i][j] == 1:
                m += 1
                f += 1
            else:
                g += 1
                f += 1
        score = 0 - abs(9-m) - abs(14-g) - abs(15-f)
        '''
        if gc%100 == 0:
            print(score)
        '''
        if score > bestScore:
            bestScore = score
            bestMember = i
        scores.append(score)
        
    if bestScore == 0:
        gradeFlag = True
    return gradeFlag, bestMember, scores

def makeChild(pA, pB, muRate):
    mu = int(1/muRate)

    child = []
    last = None
    available = [0,1,2]
    for i in range(19):
        if not randrange(mu):
            if last == None:
                last = randrange(3)
                del available[available.index(last)]
            available.append(last)
            last = available[randrange(2)]
            del available[available.index(last)]
            child.append(last)
        elif randrange(2) and pA[i] in available:
            if last == None:
                last = pA[i]
                del available[available.index(last)]
            available.append(last)
            last = pA[i]
            del available[available.index(last)]
            child.append(last)
        elif pB[i] in available:
            if last == None:
                last = pB[i]
                del available[available.index(last)]
            available.append(last)
            last = pB[i]
            del available[available.index(last)]
            child.append(last)
        else:
            if last == None:
                last = randrange(3)
                del available[available.index(last)]
            available.append(last)
            last = available[randrange(2)]
            del available[available.index(last)]
            child.append(last)
    return child

def parentSelector(n):
    if n < 0:
        return 0
    elif randrange(2):
        return n
    return parentSelector(n-1)

def parentProvider(scores, maxIndex):
    for i in range(maxIndex - parentSelector(maxIndex)):
        del scores[scores.index(max(scores))]
    return scores.index(max(scores))

def evolvePop(pop, scores, muRate, percentRandPop):
    popSize = len(pop)
    maxIndex = popSize - 1
    nonRandPopThreshold = popSize - (popSize * percentRandPop)
    newPop = []
    for i in range(popSize):
        if i > nonRandPopThreshold:
            newPop.append(getPopMember())
        else:
            pai = parentProvider(cpy(scores), maxIndex)
            pbi = parentProvider(cpy(scores), maxIndex)
            pA = pop[pai]
            pB = pop[pbi]
            child = makeChild(cpy(pA),cpy(pB), muRate)
            newPop.append(child)
    return newPop

def genetic(popSize, muRate, percentRandPop):
    pop = initPop(popSize)
    gradeFlag = False
    bestMember = 0
    scores = []
    generationCount = 0
    while gradeFlag is False:
        gradeFlag, bestMember, scores = gradePop(pop, generationCount)
        if gradeFlag is False:
            pop = evolvePop(cpy(pop), cpy(scores), muRate, percentRandPop)
        generationCount+= 1
        if generationCount % 100 == 0:
            print(generationCount, scores[bestMember])
            #print(x)
    print('Generation:', generationCount)
    print('Member:', bestMember)
    print('Sets:', pop[bestMember])
    return

#genetic(100,0.01,0.5)
