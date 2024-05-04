from errors import *

##########################################
# Values

class Number:
    # Constructor
    def __init__(self, value):
        self.value = value
        self.set_position()
        self.set_context()

    # Get position for error messages
    def set_position(self, position_start=None, position_end=None):
        self.position_start = position_start
        self.position_end = position_end
        return self
    
    def set_context(self, context=None):
        self.context = context
        return self

    # Addition
    def added_to(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None
    
    # Subtraction
    def subtracted_by(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None
        
    # Multiplication
    def multiplied_by(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None
    
    # Division
    def divided_by(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RunTimeError(other.position_start, other.position_end, 'Division by zero', self.context)
            return Number(self.value / other.value).set_context(self.context), None
    
    # Print
    def __repr__(self):
        return str(self.value)