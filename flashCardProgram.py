from random import randrange

def flashCards(fcData):
    totalScore = 0
    totalOutOf = 0
    timesPracticed = 0
    while True:
        score = 0
        outOf = 0
        fcDataCopy = []
        fcDataCopy.append(list(fcData[0]))
        fcDataCopy.append(list(fcData[1]))
        print(len(fcData[0]))
        numOfCards = len(fcDataCopy[0])
        cardsLeft = numOfCards
        print('hi')
        for i in range(numOfCards):
            x = randrange(cardsLeft)
            if randrange(2):
                print('>>',fcDataCopy[0][x])
                y = input('>< ')
                print('>>',fcDataCopy[1][x])
                if y == fcDataCopy[1][x]:
                    score += 1
            else:
                print('>>',fcDataCopy[1][x])
                y = input('>< ')
                print('>>',fcDataCopy[0][x])
                if y == fcDataCopy[0][x]:
                    score += 1
            del fcDataCopy[0][x]
            del fcDataCopy[1][x]
            cardsLeft -= 1
            outOf += 1
        print('You scored',score,'out of',outOf,', which is',
              str(int((score/outOf) * 100)) + '%')
        totalScore += score
        totalOutOf += outOf
        timesPracticed += 1
        y = input('continue? (y/n): ')
        if y == 'n':
            break
    print('Your total score is',str(totalScore) + '/' + str(totalOutOf),'=',
          str(int((totalScore/totalOutOf) * 100)) + '%')
    print('After having practiced',timesPracticed,'time(s).')
    print('Good luck!')

def createFlashCards():
    backData = ['start_date','user_id','student_id','grade','k',
                'grade_1','grade_2','grade_3','grade_4','grade_5',
                'grade_6','grade_7','grade_8','algebra']
    bdLen = len(backData)
    frontData = ['col'] * bdLen 
    for i in range(bdLen):
        frontData[i] += str(i)
    return list(frontData), list(backData)

def runFlash():
    a,b = createFlashCards()
    fcData = list([a,b])
    flashCards(fcData)
    return

runFlash()
