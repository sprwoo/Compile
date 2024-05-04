##########################################
# NODES

class NumberNode:
    # Constructor
    def __init__(self, token):
        self.token = token
        self.position_start = self.token.position_start
        self.position_end = self.token.position_end
    
    # Print
    def __repr__(self):
        return f'{self.token}'
    
# Binary operation node
# + - * /
class BinaryOpNode:
    def __init__(self, left_node, operator_token, right_node):
        self.left_node = left_node
        self.operator_token = operator_token
        self.right_node = right_node

        self.position_start = self.left_node.position_start
        self.position_end = self.right_node.position_end

    def __repr__(self):
        return f'({self.left_node}, {self.operator_token}, {self.right_node})'

# Unary operation node
# -
class UnaryOpNode:
    def __init__(self, operator_token, node):
        self.operator_token = operator_token
        self.node = node

        self.position_start = self.operator_token.position_start
        self.position_end = node.position_end
    
    def __repr__(self):
        return f'({self.operator_token}, {self.node})'