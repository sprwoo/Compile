from lexer import *
from basicparser import *
from interpreter import *
from context import *

def run(filename, text):
    # Generate Tokens
    lexer = Lexer(filename, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error

    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error

    # Run interpreter
    interpreter = Interpreter()
    context = Context('<root>')
    result = interpreter.visit(ast.node, context)

    return result.value, result.error