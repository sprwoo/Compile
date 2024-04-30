##########################################
# INTERPRETER

class Interpreter:
    def visit(self, node):
        # We will need to visit every node but we will also require
        # different methods in order to visit the different nodes

        # Create the function name
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node)