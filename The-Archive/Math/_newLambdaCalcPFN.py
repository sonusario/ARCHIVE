gDict = {"#":[3,defun]}

class tree():
    def __init__(self, pnoc, children):
        self.children

def parse(line):
    arr = line.split(" ")
    arrlen = len(arr)
    dFlag = True if arr[arrlen-1] in gDict
    tFlag = True if "'" in arr[arrlen - 1]
