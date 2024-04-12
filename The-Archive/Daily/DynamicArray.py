def dynArray():
    N, Q = map(int, input().split())
    seqList = []
    for i in range(N):
        seqList.append([])

    lastAnswer = 0
    for i in range(Q):
        qt, x, y = map(int, input().split())
        if qt-1:
            dex = (x^lastAnswer)%N
            lastAnswer = seqList[dex][y%len(seqList[dex])]
            print(lastAnswer)
        else:
            dex = (x^lastAnswer)%N
            seqList[dex].append(y)
    return
