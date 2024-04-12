import fileOpener as fo
import fileWriter as fw

arr = fo.getLines("varql.txt")
cat = ""
for item in arr:
    cat += item
fw.wrtTxtToFile("varql_out.txt",cat)
