import win32com.client as win32
import time

def tabFormat(ft,col_one,col_two):
    formatedOutput = []
    col_oneLens = []
    for i in col_one:
        col_oneLens.append(len(i))
    maxLen = max(col_oneLens)

    for i in range(len(col_one)):
        spaces = ' ' * ((maxLen - col_oneLens[i]) + 1)
        formatedOutput.append(ft + col_one[i] + spaces + col_two[i])

    return list(formatedOutput), maxLen

def guessDataTypes(colNames):
    colTypes = []
    cNameLen = len(colNames)
    '''
    for j in range(cNameLen):
        if 'date' in colNames[j]:
            colTypes.append('date')
        else:
            depth = 2
            x = None
            while x == None:
                x = str(ws.Cells(depth,j+1).Value)
                if x == 'None':
                    x = None
                depth += 1
            if '-' in x:
                if x[0] == '-' and x.replace('-','').replace(' ', '').replace('.', '').isdigit() and x.count('-') < 2:
                    colTypes.append('NUMBER(' + str(round(1.5 * len(x))) + ')')
            elif x.replace(' ', '').replace('.', '').isdigit():
                colTypes.append('NUMBER(' + str(round(1.5 * len(x))) + ')')
            else:
                colTypes.append('VARCHAR2(30 BYTE)')
        if j < cNameLen - 1:
             colTypes[j] += ','
    '''
    for i in range(cNameLen):
        colTypes.append('--INSERT DATATYPE')
        if i < cNameLen -1:
            colTypes[i] += ','
    return list(colTypes)
    #'''

def checkTen(i):
    i += 1
    flag = False
    x = ''
    tenCount = 10
    while tenCount > 0:
        x = ws.Cells(1,i).Value
        if x != None:
            flag = True
            return i,flag,x
        i += 1
        tenCount -= 1
    return i,flag,x

def getColNames():
    i = 1
    x = ''
    colNames = []
    doneFlag = False
    while x != None and x != ' ':
        x = ws.Cells(1,i).Value
        if x != None and x != ' ':
            colNames.append(x)
        else:
            i,doneFlag,x = checkTen(i)
            if x != None and x != ' ':
                colNames.append(x)
        if not doneFlag:
            break
        i += 1
    return list(colNames)

def cols_to_rows_txt():
    txtFile = open(r'rowFile2.txt', 'w+')
    colNames = getColNames()
    for i in colNames:
        txtFile.write(i + '\n')
    txtFile.close()

def makeFields():    
    colNames = getColNames()
    colTypes = guessDataTypes(colNames)
    formatedFields,x = tabFormat('\t',colNames,colTypes)
    return list(formatedFields)

def makeCode():
    codeFile = open(r'csFile2.sql', 'w+')
    #print('CREATE TABLE /*<put table name here>*/ (')
    codeFile.write('CREATE TABLE /*<put table name here>*/ (' + '\n')
    #print('--The datatypes for the below field name will more than likely need to be changed')
    #codeFile.write('--The datatypes for the below field name will more than likely need to be changed' + '\n')
    fields = makeFields()
    for i in fields:
        #print(i)
        codeFile.write(i + '\n')
    #print(')')
    codeFile.write(')' + '\n')
    #print('TABLESPACE /*<database>*/')
    codeFile.write('TABLESPACE /*<database>*/' + '\n')
    settingNames = ['PCTUSED','PCTFREE','INITRANS','MAXTRANS','STORAGE']
    settingValues = ['0','10','1','255','(']
    settings,x = tabFormat('',settingNames,settingValues)
    for i in settings:
        #print(i)
        codeFile.write(i + '\n')
    settingNames = ['INITIAL','NEXT','MINEXTENTS','MAXEXTENTS','PCTINCREASE','BUFFER_POOL']
    settingValues = ['64k','1M','1','UNLIMITED','0','DEFAULT']
    settings,y = tabFormat('\t\t\t',settingNames,settingValues)
    for i in settings:
        #print(i)
        codeFile.write(i + '\n')
    #print((' ' * (x + 1)) + ')')
    codeFile.write((' ' * (x+1)) + ')' + '\n')
    #print('LOGGING\nNOCOMPRESS\nNOCACHE\nMONITORING;')
    codeFile.write('LOGGING\nNOCOMPRESS\nNOCACHE\nMONITORING;' + '\n')
    codeFile.close()
    return

def scriptStarter():
    global ws
    print('Code maker started...')
    filePath = input('Enter path to file: ')
    fileName = input('Enter name of file: ') + '.csv'
    startTime = time.time()
    excel = win32.gencache.EnsureDispatch('Excel.Application')
    #excel.Visible = True
    wb = excel.Workbooks.Open(filePath + '\\' + fileName)
    if 'wichita' in fileName:
        ws = wb.Worksheets('20171003_wichita_student_profic')
    else:
        ws = wb.Worksheets('readingplus')

    makeCode()
    cols_to_rows_txt()
    endTime = time.time()
    print('Done!')
    print('Completed in:',endTime-startTime,'seconds')
    input('Press enter to exit... ')
    wb.Close(True)

ws = ''

scriptStarter()
