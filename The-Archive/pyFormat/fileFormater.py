import fileOpener as fo
import fileWriter as fw

def lines(in_file="plain.txt"):
    return fo.getLines(in_file)

def write(concated_lines, out_file="formated.txt"):
    fw.wrtTxtToFile(out_file,concated_lines)
    return

def comma_d():
    arr = lines()
    cat = ""
    for item in arr[:-1]:
        cat += item + ",\n"
    cat += arr[-1]
    write(cat)
    return

def comma_d_quotes():
    arr = lines()
    cat = ""
    for item in arr[:-1]:
        cat += "'" + item + "',\n"
    cat += "'" + arr[-1] + "'"
    write(cat)
    return

def remove_commas():
    arr = lines()
    cat = ""
    for item in arr:
        for word in item.split(" "):
            if "," not in word:
                cat += word + "\n"
            else:
                cat += word[:-1] + "\n"
    write(cat)
    return

def remove_commits():
    arr = lines()
    cat = ""
    for item in arr[:-1]:
        if "commit" not in item: cat += item + "\n"
    if "commit" not in arr[-1]: cat += item
    write(cat)
    return

def remove_spec(n):
    arr = lines()
    cat = ""
    for item in arr[:-1]:
        cat += item[:n].strip() + "\n"
    cat += arr[-1][:n].strip()
    write(cat)
    return

def last_first_d_quotes():
    arr = lines()
    catL = ""
    catF = ""
    for item in arr[:-1]:
        catL += "'" + item.split(", ")[0] + "',\n"
        catF += "'" + item.split()[1] + "',\n"
    catL += "'" + item.split(", ")[0] + "'"
    catF += "'" + item.split()[1] + "'"
    cat = "Last Names:\n" + catL + "\n\nFirst Names:\n" + catF
    write(cat)
    return

def remove_names_d_quotes():
    arr = lines()
    cat = ""
    for item in arr[:-1]:
        cat += "'" + item[0:5] + "',\n"
    cat += "'" + arr[-1] + "'"
    write(cat)
    return

