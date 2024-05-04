from values import *
from tokens import *
from errors import *
from context import *

##########################################
# INTERPRETER

class Interpreter:
    def visit(self, node, context):
        # We will need to visit every node but we will also require
        # different methods in order to visit the different types of nodes

        # Create the function name
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context)
    
    def no_visit_method(self, node, context):
        raise Exception(f'No visit_{type(node).__name__} method defined')
    
    # Number Node
    def visit_NumberNode(self, node, context):
        return RunTimeResult().success(Number(node.token.value).set_context(context).set_position(node.position_start, node.position_end))

    # Binary Operator Node
    def visit_BinaryOpNode(self, node, context):
        runtime_result = RunTimeResult()
        # We must visit both left and right nodes to apply the operation
        left = runtime_result.register(self.visit(node.left_node, context))
        if runtime_result.error: return runtime_result
        right = runtime_result.register(self.visit(node.right_node, context))
        if runtime_result.error: return runtime_result

        # Find and apply the operation
        if node.operator_token.type == TT_ADD:
            result, error = left.added_to(right)
        if node.operator_token.type == TT_MINUS:
            result, error = left.subtracted_by(right)
        if node.operator_token.type == TT_MUL:
            result, error = left.multiplied_by(right)
        if node.operator_token.type == TT_DIV:
            result, error = left.divided_by(right)
        
        if error:
            return runtime_result.failure(error)
        else:
            return runtime_result.success(result.set_position(node.position_start, node.position_end))

    
    # Unary Operator Node
    def visit_UnaryOpNode(self, node, context):
        runtime_result = RunTimeResult()
        number = runtime_result.register(self.visit(node.node, context))
        if runtime_result.error: return runtime_result
        error = None

        # Only unary operator is negation
        if node.operator_token.type == TT_MINUS:
            number, error = number.multiplied_by(Number(-1))
        if error:
            return runtime_result.failure(error)
        else:
            return runtime_result.success(number.set_position(node.position_start, node.position_end))