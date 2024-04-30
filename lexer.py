from tokens import *
from position import *
from errors import *

DIGITS = "0123456789"

##########################################
# LEXER

class Lexer:
    # Constructor
    def __init__(self, filename, text):
        self.filename = filename
        self.text = text
        self.position = Position(-1, 0, -1, filename, text)
        self.current_char = None
        self.advance()
    
    # Advance to the next character
    def advance(self):
        self.position.advance(self.current_char)
        self.current_char = self.text[self.position.idx] if self.position.idx < len(self.text) else None

    # Create the tokens
    def make_tokens(self):
        tokens = []
        while self.current_char != None:
            if self.current_char in ' \t':
                # Skip if it is either a whitespace or tab
                pass
            elif self.current_char in DIGITS:
                # If the character is a number, we will read in every subsequent number
                # to form one number
                tokens.append(self.make_number())

            # Basic operators
            elif self.current_char == '+':
                tokens.append(Token(TT_ADD, position_start = self.position))

            elif self.current_char == '-':
                tokens.append(Token(TT_MINUS, position_start = self.position))

            elif self.current_char == '*':
                tokens.append(Token(TT_MUL, position_start = self.position))

            elif self.current_char == '/':
                tokens.append(Token(TT_DIV, position_start = self.position))

            elif self.current_char == '(':
                tokens.append(Token(TT_OPEN, position_start = self.position))

            elif self.current_char == ')':
                tokens.append(Token(TT_CLOSE, position_start = self.position))
                
            else:
                position_start = self.position.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(position_start, self.position, "'" + char + "'")
            self.advance()

        # Attach the end of file token once done reading in all characters in the file
        tokens.append(Token(TT_EOF, position_start = self.position))
        return tokens, None
    
    def make_number(self):
        num_str = ''
        dot_count = 0
        position_start = self.position.copy()

        # Read in every subsequent number, as well as any decimal points to form one number
        while self.current_char != None and self.current_char in DIGITS + '.':
            if self.current_char == '.':
                if dot_count == 1: break
                dot_count += 1
                num_str += '.'
            else:
                num_str += self.current_char
            self.advance()
        
        # Return it as an integer if there are no decimals, otherwise as a float
        if dot_count == 0:
            return Token(TT_INT, int(num_str), position_start, self.position)
        else:
            return Token(TT_FLOAT, float(num_str), position_start, self.position)