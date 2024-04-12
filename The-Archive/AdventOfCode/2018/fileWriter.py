import os

workingDir = os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))

def wrtTxtToFile(fname, txt):
    f = open(workingDir + "\\" + fname, "w")
    f.write(txt)
    
