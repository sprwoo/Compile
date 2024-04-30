from string_with_arrows import *

##########################################
# ERRORS

class Error:
    # Constructor
    def __init__(self, position_start, position_end, error_name, details):
        self.position_start = position_start
        self.position_end = position_end
        self.error_name = error_name
        self.details = details
    
    # Create error message
    def as_string(self):
        result = f'{self.error_name}: {self.details}\n'
        result += f'File {self.position_start.fn}, line {self.position_start.ln + 1}'
        result += '\n\n' + string_with_arrows(self.position_start.ftxt, self.position_start, self.position_end)
        return result

# Illegal character error
class IllegalCharError(Error):
    def __init__(self, position_start, position_end, details):
        super().__init__(position_start, position_end, 'Illegal Character', details)

# Invalid syntax error
# e.g. "1 + + 2", "2 1 +" 
class InvalidSyntaxError(Error):
    def __init__(self, position_start, position_end, details):
        super().__init__(position_start, position_end, 'Invalid Syntax', details)
