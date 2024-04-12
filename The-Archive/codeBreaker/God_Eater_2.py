#solved by someone else

s  = 'CGOAHWJDYKVFKYZSUCTVIWKSUXCKYZSJJO'

notes = ['e2','b2','g2','f2','d3']

def partitions(s):
    if s:
        for i in range(1, len(s) + 1):
            for p in partitions(s[i:]):
                yield [s[:i]] + p
    else: yield []
    return
