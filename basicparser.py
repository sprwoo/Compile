from errors import *
from tokens import *
from nodes import *

##########################################
# PARSE RESULT

# ParseResult tells us if there is a parsing error
class ParseResult:
    # Constructor
    def __init__(self):
        self.error = None
        self.node = None
    
    # result is either a ParseResult or Node
    def register(self, result):
        # Check if result is a ParseResult
        if isinstance(result, ParseResult):
            # Return the error is result represents an error
            if result.error: self.error = result.error
            return result.node
        
        # Return the node
        return result
    
    # Successful parse
    def success(self, node):
        self.node = node
        return self
    
    # Failure in parsing
    def failure(self, error):
        self.error = error
        return self

##########################################
# PARSER

class Parser:
    # Constructor
    def __init__(self, tokens):
        self.tokens = tokens
        self.token_idx = -1
        self.advance()
    
    # Advance tokens
    def advance(self):
        self.token_idx += 1

        # Return tokens while it is within the array of tokens we need to process
        if self.token_idx < len(self.tokens):
            self.current_token = self.tokens[self.token_idx]
        return self.current_token

    # Parse every token in the array until it reaches the end of the file
    def parse(self):
        result = self.expr()
        if not result.error and self.current_token.type != TT_EOF:
            # Return a syntax error if result is an error
            return result.failure(InvalidSyntaxError(self.current_token.position_start, self.current_token.position_end, 
                               "Expected '+', '-', '*' or '/'"))
        return result

    # A factor is int/float
    # It also sorts out the order of operations we must do
    def factor(self):
        result = ParseResult()
        token = self.current_token
        
        # If token is +/-, 
        if token.type in (TT_ADD, TT_MINUS):
            result.register(self.advance())
            factor = result.register(self.factor())
            if result.error: return result
            return result.success(UnaryOpNode(token, factor))

        # If the token is a number, we can return a successful parse and a NumberNode
        elif token.type in (TT_INT, TT_FLOAT):
            result.register(self.advance())
            return result.success(NumberNode(token))
        
        # If token is an open bracket, we need to evaluate these first
        # Advance until we find the close bracket, otherwise return an error 
        elif token.type == TT_OPEN:
            result.register(self.advance())
            expr = result.register(self.expr())
            if result.error: return result
            if self.current_token.type == TT_CLOSE:
                result.register(self.advance())
                return result.success(expr)
            
            # Return an error
            else: return result.failure(InvalidSyntaxError(self.current_token.position_start, self.current_token.position_end,
                                                        "Expected ')'"))
        
        return result.failure(InvalidSyntaxError(token.position_start, token.position_end, "Expected int or float"))
    
    # Find the "terms" of the equation by looking for * or /
    def term(self):
        return self.binary_op(self.factor, (TT_MUL, TT_DIV))

    # Find the "expressions" of the equations by looking for + or -
    def expr(self):
        return self.binary_op(self.term, (TT_ADD, TT_MINUS))
    
    # Evaluate the binary operations
    def binary_op(self, func, operators):
        result = ParseResult()

        # Grab the left factor/term
        left = result.register(func())
        if result.error: return result

        # Check if the current token's type is the ones we are looking for
        while self.current_token.type in operators: 
            operator_token = self.current_token
            result.register(self.advance())

            # Grab the right factor/term
            right = result.register(func())
            if result.error: return result

            left = BinaryOpNode(left, operator_token, right)
        return result.success(left)
