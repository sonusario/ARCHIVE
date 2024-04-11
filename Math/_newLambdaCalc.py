scope = {}

def parenBalanced(line):
    pTracker = 0
    pUpFlag = False
    pDownFlag = False
    spaceCount = 0
    for i in range(len(line)):
        x = line[i]
        if x == "(":
            if pUpFlag and (pTracker == 0):
                print("Paren scoping error!")
                return False
            pTracker += 1
            if not pUpFlag: pUpFlag = True
        if x == ")": pTracker -= 1
        if x == " ": spaceCount += 1

        if pTracker < 0:
            print("Non matching parens!")
            return False
    if not (pTracker == 0):
        print("Non matching parens!")
        return False
    if not pUpFlag and spaceCount > 0:
        print("Non atomic input!")
        return False
    return True

def parse(line):
    if "' " in line:
        print("Floating tic(') error!")
    arr = line.split(" ")
    arrLen = len(arr)
    if arrLen == 0: return ""
    if not parenBalanced(line): return
    if arr[0] == "'(": return " ".join(arr)
    return

def decon(line):
    parse(line)
    return
