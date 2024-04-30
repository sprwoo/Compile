from lexer import *
from basicparser import *

def run(filename, text):
    # Generate Tokens
    lexer = Lexer(filename, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()

    return ast.node, ast.error
