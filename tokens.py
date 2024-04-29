##########################################
# TOKENS

TT_INT = 'TT_INT'
TT_FLOAT = 'FLOAT'
TT_ADD = 'ADD'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_OPEN = 'OPEN'
TT_CLOSE = 'RCLOSE'
TT_EOF = 'EOF'

class Token: 
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()
        
        if pos_end:
            self.pos_end = pos_end

    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'