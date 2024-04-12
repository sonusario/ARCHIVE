def mk_sdAddr_set():
    for i in range(10):
        line = str(i) + ' '
        for j in range(10):
            line += str(j) + " sd_add @" + (' ' + str(i) + ' ' if j != 9 else ' ')
            if j == 9:
                print("\t" + line)

def mk_sdAdd_cmpr():
    for i in range(10):
        line = ""
        for j in range(10):
            line += str(i + j)[::-1][0] + (' ' if j != 9 else '')
            if j == 9:
                print("\t" + line)

def mk_pOne_set():
    for i in range(10):
        print(i,"plus_one_c @")
