from random import randrange
'''
x = 10000
f = (lambda a: lambda v: 0 if not v else a(a,v))(lambda b,w: w if randrange(2) else b(b,w-1))
sum(list(map(lambda a: 1 if a==10 else 0, list(map(f,[10]*x)))))/x
'''
#[32,127)
functionKey = [[[0,1],[2,3]],[[4,5],[6,7]]]

class cell:
    def __init__(self):
        function = list(
            map(
                lambda x: chr(x),
                list(
                    map(
                        lambda x: randrange(32,127),
                        [0]*8
                        )
                    )
                )
            )
