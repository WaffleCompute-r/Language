SYMBOL_CHARS = ['+', '|', '=']

def lex_num(line): #done
    num = ""
    # iterate through the line
    for c in line:
        # if the character is not a digit
        if not c.isdigit():
            break
        # add the digit to num
        num += c
        
    return 'num', int(num), len(num)

def lex_str(line): #done
    delimiter = line[0]
    string = ""
    # iterate through the line
    for c in line:
         #adds each character to the string
         string += c
    return 'str', string, len(string)

def lex_sym(line):
    symbol = ""
    for c in line:
        if c not in SYMBOL_CHARS:
            break
        symbol += c

    return 'sym', symbol, len(symbol)

def lex_id(line): #done
    # keywords
    keys = ['print', 'while', 'if', 'elif', 'else']
    # id is a name assigned by the user (variable name)
    id = ""
    # iterate through the line
    for c in line:
        # if the character is not a digit, letter, or underscore
        if not (c.isdigit() or c.isalpha() or c == "_"):
            break
        id += c
    if id in keys:
        # keyword
        return 'key', id, len(id)
    else:
        # variable name
        return 'ID', id, len(id)

def lex(line): #done
    count = 0
    while count < len(line):
        lexeme = line[count]
        if lexeme.isdigit():
            #variables: type, token, consmued
            #consumed is thee length of the token
            #sets those variables to the return values of the function lexNum
            # line[count:] is the substring of line from count to the end
            typ, tok, consumed = lex_num(line[count:])
            count += consumed
        elif lexeme == '"' or lexeme == "'":
            typ, tok, consumed = lex_str(line[count:])
            count += consumed
        elif lexeme.isalpha():
            typ, tok, consumed = lex_id(line[count:])
            count += consumed
        elif lexeme in SYMBOL_CHARS:
            typ, tok, consumed = lex_sym(line[count:])
            count += consumed
        else:
            # does this actually do anything
            # it'll just print the stuff from the last time round
            count += 1
    
        print("type: ", typ, "token: ", tok, "consumed: ", consumed)
        
code = input()
lex(code)