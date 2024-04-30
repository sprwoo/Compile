from position import *

##########################################
# TOKENS

# Token types
TT_INT = 'TT_INT'       # Integer
TT_FLOAT = 'FLOAT'      # Float
TT_ADD = 'ADD'          # Addition
TT_MINUS = 'MINUS'      # Subtraction / Negation
TT_MUL = 'MUL'          # Multiplication
TT_DIV = 'DIV'          # Division
TT_OPEN = 'OPEN'        # Open bracket
TT_CLOSE = 'RCLOSE'     # Close bracket
TT_EOF = 'EOF'          # End of File

class Token: 
    # Constructor
    def __init__(self, type_, value=None, position_start=None, position_end=None):
        self.type = type_
        self.value = value

        # If position_start/end was given, initialize it as given
        if position_start:
            self.position_start = position_start.copy()
            self.position_end = position_start.copy()
            self.position_end.advance()
        
        if position_end:
            self.position_end = position_end

    # Print
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'