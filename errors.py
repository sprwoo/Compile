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

# Runtime errors
class RunTimeError(Error):
    def __init__(self, position_start, position_end, details, context):
        super().__init__(position_start, position_end, 'Runtime Error', details)
        self.context = context
    
    # Override the other as_string function to include contexts
    def as_string(self):
        result = self.generate_traceback()
        result += f'{self.error_name}: {self.details}\n'
        result += '\n\n' + string_with_arrows(self.position_start.ftxt, self.position_start, self.position_end)
        return result

    # Get the context chain
    def generate_traceback(self):
        result = ''
        position = self.position_start
        context = self.context
        
        while context:
            result = f'  File {position.fn}, line {str(position.ln + 1)}, in {context.display_name}\n' + result
            position = context.parent_entry_position
            context = context.parent
        
        return 'Traceback (most recent call last):\n' + result

class RunTimeResult:
    def __init__(self):
        self.value = None
        self.error = None

    def register(self, result):
        if result.error: self.error = result.error
        return result.value
    
    def success(self, value):
        self.value = value
        return self
    
    def failure(self, error):
        self.error = error
        return self
