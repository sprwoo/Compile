##########################################
# NODES

class NumberNode:
    # Constructor
    def __init__(self, token):
        self.token = token
    
    # Print
    def __repr__(self):
        return f'{self.token}'
    
# Binary operation node
# + - * /
class BinOpNode:
    def __init__(self, left_node, operator_token, right_node):
        self.left_node = left_node
        self.operator_token = operator_token
        self.right_node = right_node

    def __repr__(self):
        return f'({self.left_node}, {self.operator_token}, {self.right_node})'

# Unary operation node
# -
class UnaryOpNode:
    def __init__(self, operator_token, node):
        self.operator_token = operator_token
        self.node = node
    
    def __repr__(self):
        return f'({self.operator_token}, {self.node})'