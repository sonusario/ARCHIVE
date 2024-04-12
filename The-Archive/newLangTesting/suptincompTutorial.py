def tokenizer(inFileStr):
    current = 0
    tokens = []
    fileLen = len(inFileStr)
    
    while current < fileLen:
        char = inFileStr[current]

        if char == '(':
            tokens.append({
                    "type": 'paren',
                    "value": '(',
                })
            current += 1
            continue

        if char == ')':
            tokens.append({
                    "type": 'paren',
                    "value": ')',
                })
            current += 1
            continue

        if char.isspace():
            current += 1
            continue

        if char.isdigit():
            value = ''
            while char.isdigit():
                value += char
                current += 1
                if current >= fileLen: char = ''
                else: char = inFileStr[current]
            tokens.append({
                    "type": 'number',
                    "value": value
                })
            continue

        if char == '"':
            value = ''
            current += 1
            if current >= fileLen: char = ''
            else: char = inFileStr[current]
            while char != '"':
                value += char
                current += 1
                if current >= fileLen: break
                else: char = inFileStr[current]
            if char != '"':
                raise Exception('Miss matched \'"\'s, please modify code.')
            tokens.append({
                    "type": 'string',
                    "value": value
                })
            current += 1
            continue

        if char.isalpha():
            value = ''
            while char.isalpha():
                value += char
                current += 1
                if current >= fileLen: char = ''
                else: char = inFileStr[current]
            tokens.append({
                    "type": 'name',
                    "value": value
                })
            continue

        raise Exception(" I don't know what this character is:", char)
    return tokens

def parser(tokens):
    current = 0

    def walk():
        token = tokens[current]
        if token["type"] == 'number':
            current += 1
            return {
                "type": 'NumberLiteral',
                "value": token["value"]
            }

        if token["type"] == 'string':
            current += 1
            return {
                "type": 'StringLiteral',
                "value": token["value"]
            }

        if token["type"] == 'paren' and token["value"] == '(':
            current += 1
            token = tokens[current]

            node = {
                "type": 'CallExpression',
                "name": token["value"],
                "params": []
            }
