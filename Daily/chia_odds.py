from math import ceil as roundup

def p(ms,ns):
    return (ms/1000)/ns

def odds(ms,ns):
    pw = p(ms,ns)
    oa = (1-pw)/pw
    print('Odds of winning a challenge are 1:' + str(roundup(oa)))
    print(u'Estimated Time to Win \u2248 ' + str(roundup(oa/4608)), 'days')
    print('You\'ve been struck by lightning', roundup(oa/15300),'times.')
