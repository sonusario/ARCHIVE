def startDef(tokens, current, tLen):
    while current < tLen:
        token = tokens[current]
        if token == ":":
            defStr = token
            depth = 1
            while depth > 0:
                current += 1
                try:
                    token == tokens[current]
                except:
                    raise Exception("Reached EOF before finding matching ';'.")
                if token == ":": depth += 1
                elif token == ";": depth -= 1
                defStr += ' ' + token
            

keyWords = {
        ":": startDef,
        ";": endDef,
        "'": quote
    }
theDictionary = {}
theStack = []

def tokenizer(inStr):
    return inStr.split(' ')

def parser(tokens):
    current = 0
    tLen = len(tokens)

    while current < tLen:
        token = tokens[current]

        if token == ":":
            current = keyWords[":"](tokens, current+1, tLen)
