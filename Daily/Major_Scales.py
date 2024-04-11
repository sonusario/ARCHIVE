noteNames = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
solfNames = ['Do','Re','Mi','Fa','So','La','Ti']
majorDict = {'C':0,'C#':1,'D':2,'D#':3,'E':4,'F':5,'F#':6,'G':7,'G#':8,'A':9,'A#':10,'B':11}
solfDict = {'Do':0, 'Re':2, 'Mi':4, 'Fa':5, 'So':7, 'La':9, 'Ti':11}

def majorSolfNote(major, solf):
    n = majorDict[major] + solfDict[solf]
    if n > 11:
        n -= 12
    return noteNames[n]

def runScales():
    for i in range(12):
        for j in range(7):
            print(noteNames[i], solfNames[j], ':', majorSolfNote(noteNames[i], solfNames[j]))
    return

#runScales()

cScale = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
sDict = {'Do':0, 'Re':2, 'Mi':4, 'Fa':5, 'So':7, 'La':9, 'Ti':11}

def note(major, solf):
    return cScale[(cScale.index(major) + sDict[solf])%12]

def runScales2():
    for i in range(12):
        for key in sDict:
            print(cScale[i], key, ':', note(cScale[i], key))
    return

#runScales2()
