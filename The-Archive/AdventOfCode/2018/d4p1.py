import fileOpener as fo

def makeRecordDictionary(plainRecords):
    rd = {}
    for record in plainRecords:
        date = record[1:11]
        time = record[12:17]
        msg = record[19:len(record)]
        if date not in rd:
            rd[date] = {}
            rd[date][time] = msg
        else:
            rd[date][time] = msg
    return rd

def makeChronology(recordDict):
    previousGuard = None
    currentGuard = None
    mostSleeping = None
    guardTracker[currentGuard] = {}
    guardTracker[currentGuard]["totalSleepMins"] = 0
    guardTracker[currentGuard]["minSleptMost"] = None
    for i in range(60):
        guardTracker[currentGuard][i] = 0
    awake = True
    month = 1
    while month <= 12:
        dINm = [0,31,28,31,30,31,30,31,31,30,31,30,31][month]
        day = 1
        while day <= dINm:
            date = "1518-" + "{:0>2d}".format(month) + "-" + "{:0>2d}".format(day)
            if date in recordDict:
                hrCode = 0
                while hrCode < 2:
                    hour = [23,0][hrCode]
                    minute = 0
                    while minute < 60:
                        time = "{:0>2d}".format(hour) + ":" + "{:0>2d}".format(minute)
                        if time in recordDict[date]:
                            msg = recordDict[date][time]
                            if "Guard" in msg:
                                previousGuard = currentGuard
                                currentGuard = msg.split(' ')[1]
                                if currentGuard not in guardTracker:
                                    guardTracker[currentGuard] = {}
                                    guardTracker[currentGuard]["totalSleepMins"] = 0
                                    guardTracker[currentGuard]["minSleptMost"] = None
                                    for i in range(60):
                                        if hrCode == 0:
                                            guardTracker[currentGuard][i] = 0
                                        elif i <= minute:
                                            guardTracker[currentGuard][i] = 1
                                else:
                                    if hrCode == 0:
                                        for i in range(minute,60):
                                            guardTracker[previousGuard][i] += 0 if awake else 1
                                        if day+1 == dINm: day = 1
                                        hrCode = 1
                                        minute = 0
                                        if
                            elif "falls" in msg:
                                awake = False
                            elif "wakes" in msg:
                                awake = True

def getRecords():
    plainRecords = fo.getLines("d4p1.txt")
    recordDict = makeRecordDictionary(plainRecords)
    chronologyOfRecords = makeChronology(recordDict)
    return
