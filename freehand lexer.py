class lexer:
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

    symbols = ["+", "-", "*", "/"]

    def lex_sym(self, line):
        symbol = ""
        for c in line:
            if c not in self.symbols:
                break
            symbol += c

        return 'SYM', symbol, len(symbol)

    def lex_id(self, line):
        keys = ['print', 'while', 'if', 'elif', 'else']
        id = ""
        for c in line:
            if not c.isalpha():
                break
            id += c
        if id in keys:
            return 'key', id, len(id)
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
        print(tokens)

code = input("")

# Create an instance of the lexer class
lexer_instance = lexer()

# Lex the user's code
lexer_instance.lex(code)