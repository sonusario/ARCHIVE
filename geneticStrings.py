from random import randrange
import time #time.time()

def parentSelector(n):
    if n < 0:
        return 0
    elif randrange(2):
        return n
    return parentSelector(n-1)

def parentProvider(scoresCopy, maxIndex):
    sCC = list(scoresCopy)
    for i in range(maxIndex - parentSelector(maxIndex)):
        del sCC[sCC.index(max(sCC))]
    return sCC.index(max(sCC))

def matchString(string, popSize, mutationRate, percentRandPop):
    maxIndex = popSize - 1
    nonRandPop = popSize - (popSize * percentRandPop)
    generation = 0
    underChar = 32 #overChar = 1114112 ##chr() can't handle this number
    overChar = 127 #overChar = 65536 ## print(chr()) can't handle this number
    #underChar = 48
    #overChar = 50
    printFreq = popSize #* 1000000
    subPrintFreq = int(printFreq / 10)

    useBucket = 0
    
    strLen = len(string)
    population = []
    scores = []
    percentCorrect = []
    bucket = []
    generation += 1
    for i in range(popSize):
        population.append('')
        scores.append(0)
        for j in range(strLen):
            c = chr(randrange(underChar, overChar))
            population[i] += c
            if c == string[j]:
                scores[i] += 1
        percentCorrect.append(round((scores[i]/strLen) * 100))
        if useBucket:
            for j in range(percentCorrect[i] + 1):
                bucket.append(i)

    #print(bucket)
    
    while True:
        scoresCopy = list(scores)
        #print(population[scores.index(max(scores))])
        newPop = []
        scores = []
        generation += 1
        if generation % printFreq == 0:
            print('')
            print('')
            print('')
        for i in range(popSize):
            if useBucket:
                pai = bucket[randrange(len(bucket))]
                pbi = bucket[randrange(len(bucket))]
            else:
                pai = parentProvider(scoresCopy, maxIndex)
                pbi = parentProvider(scoresCopy, maxIndex)
            pA = population[pai]
            pB = population[pbi]
            child = ''
            scores.append(0)
            for j in range(strLen):
                c = ''
                if randrange(2):     #either of these seem to work fine
                #if j < int(strLen/2): #either of these seem to work fine
                    c = pA[j]
                else:
                    c = pB[j]
                if not randrange(int(1/mutationRate)) or i > nonRandPop:
                    c = chr(randrange(underChar, overChar))
                child += c
                if c == string[j]:
                    scores[i] += 1
            percentCorrect[i] = round((scores[i]/strLen) * 100)
            newPop.append(child)
            #print(i, child, pai, pbi)
            #if pai > 75 or pbi > 75:
                #print(i, child, pai, pbi, generation)
            if child == string:
                print(i, child, pai, pbi)
                return generation
            elif (generation % printFreq) == 0 and (i % subPrintFreq) == 0:
                spaces = ' ' * (len(str(i)) - 1)
                print('========================')
                print('Generation:', generation)
                print('Target string:' + spaces + string)
                print('Individual ' + str(i) + ': ' + child)
                if i == (printFreq - subPrintFreq):
                    print('------------------------')
                    print('Population Avg:', sum(percentCorrect)/popSize)
                    print('------------------------')
        if useBucket:
            bucket = []
            for i in range(popSize):
                for j in range(percentCorrect[i] + 1):
                    bucket.append(i)
        #if (generation % printFreq) == 0:
            #nonRandPop *= .98
        population = list(newPop)
        if generation > 10000:
            break
    return

def runGeneticSolver(inString, PRP):
    populationSize = 150
    mutationRate = 1 / 95    #0.01
    percentRandomPopulation = PRP
    print(matchString(inString, populationSize, mutationRate, percentRandomPopulation))
    return

def geneticRunner(PRP):
    string = 'Sterling' * 15
    #string = 'To be or not to be.'
    #string = 'Ster'
    #string = '1001001010010010100100101001001'
    print('=' * 42)
    print('=' * 42)
    print('PRP:', PRP)
    print('-' * 21)
    startTime = time.time()
    runGeneticSolver(string, PRP)
    endTime = time.time()
    elapsedTime = endTime - startTime
    print('Total time:', elapsedTime)
    print('Total time x 4 = ', elapsedTime * 4)
    print('=' * 42)
    print('=' * 42)

def looper(PRP):
    while PRP < 0.65:
        geneticRunner(PRP)
        PRP += 0.01
    return

#looper(0.40)
geneticRunner(0.50)
