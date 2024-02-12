# Lexer

class Lexer:
    def __init__(self):
        self.symbols = ["+", "-", "*", "/"]
        self.keys = ['print', 'while', 'if', 'elif', 'else']

    #handles number tokens
    def lex_num(self, line):
        num=""
        #c is the character in that position
        for c in line:
            if not c.isdigit():
                break
            #build up num
            num+=c
        return 'NUM', num, len(num)

    def lex_str(self, line):
        delimiter = line[0]  # The quote character that starts the string
        string = ""
        for i, c in enumerate(line[1:], start=1):  # Skip the opening quote
            if c == delimiter:  # If we've reached the closing quote
                return 'STR', string, i + 1  # Return the string token and its length (including the quotes)
            string += c
        # If we get here, the string was not closed
        raise SyntaxError("Close your strings, you fool!")

    def lex_sym(self, line):
        symbol = ""
        for c in line:
            if c not in self.symbols:
                break
            symbol += c

        return 'SYM', symbol, len(symbol)

    def lex_id(self, line):
        id = ""
        for c in line:
            if not c.isalpha():
                break
            id += c
        if id in self.keys:
            return 'KEY', id, len(id)
        else:
            return 'ID', id, len(id)

    # lex the line
    def lex(self, line):
        tokens = []
        count = 0
        while count < len(line):
            lexeme=line[count]
            if lexeme.isdigit():
                typ, tok, consumed = self.lex_num(line[count:])
                count += consumed
                # print("typ: ", typ, ", tok: ", tok, ", len: ", consumed)
                tokens.append((typ, tok))
            elif lexeme == '"' or lexeme == "'":
                typ, tok, consumed = self.lex_str(line[count:])
                count += consumed
                # print("typ: ", typ, ", tok: ", tok, ", len: ", consumed)
                tokens.append((typ, tok))
            elif lexeme in self.symbols:
                typ, tok, consumed = self.lex_sym(line[count:])
                count += consumed
                # print("typ: ", typ, ", tok: ", tok, ", len: ", consumed)
                tokens.append((typ, tok))
            elif lexeme.isalpha():
                typ, tok, consumed = self.lex_id(line[count:])
                count += consumed
                # print("typ: ", typ, ", tok: ", tok, ", len: ", consumed)
                tokens.append((typ, tok))
            else:
                count += 1
        return tokens
    
    # all token types: NUM, STR, SYM, ID, KEY
    
# Parser
    
class Parser:
    def __init__(self, tokens):
        # stores the tokens that the lexer is providing
        self.tokens = tokens
        # stores the current token that we are parsing
        self.current_token = None
        # stores the next token that we will parse
        self.next_token()

    def next_token(self):
        try:
            self.current_token = next(self.tokens)
        # If we run out of tokens, set the current token to None
        # if there is an error, the except block will run
        except StopIteration:
            self.current_token = None

    def parse(self):
        # set result to 0
        result = 0

        # while there are still tokens to parse
        while self.current_token != None:
            #if the current token is a number add it to the result
            if self.current_token[0] == 'NUM':
                # NUM is the type of token, and the second element is the actual token
                result += int(self.current_token[1])
            # if the current token is a symbol
            if self.current_token[0] == 'SYM':
                pass
            # if the current token is a string
            if self.current_token[0] == 'STR':
                pass
            # if the current token is an identifier
            if self.current_token[0] == 'ID':
                pass
            # if the current token is a keyword
            if self.current_token[0] == 'KEY':
                pass
            # otherwise raise an error
            else:
                raise SyntaxError("This token type is not in my list of valid token types")



code = input("")

# Create an instance of the lexer class
lexer_instance = Lexer()

# Lex the user's code
lexer_instance.lex(code)