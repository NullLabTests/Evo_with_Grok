# Domains: text processing, mathematics
import ast

def tentacle(expression):
    """
    Evaluate a logical expression given as a string.
    
    Args:
    expression (str): A string containing a logical expression.
    
    Returns:
    bool: The result of the evaluated expression as a boolean value.
    
    Examples:
    >>> tentacle('True and False')
    False
    >>> tentacle('not (True or False)')
    False
    >>> tentacle('True and (False or True)')
    True
    """
    try:
        # Parse the expression into an Abstract Syntax Tree
        tree = ast.parse(expression, mode='eval')
        
        # Define a custom NodeTransformer to handle logical operators
        class LogicalTransformer(ast.NodeTransformer):
            def visit_BoolOp(self, node):
                if isinstance(node.op, ast.And):
                    return ast.Call(
                        func=ast.Name(id='all', ctx=ast.Load()),
                        args=[ast.List(elts=node.values, ctx=ast.Load())],
                        keywords=[]
                    )
                elif isinstance(node.op, ast.Or):
                    return ast.Call(
                        func=ast.Name(id='any', ctx=ast.Load()),
                        args=[ast.List(elts=node.values, ctx=ast.Load())],
                        keywords=[]
                    )
                return node
            
            def visit_UnaryOp(self, node):
                if isinstance(node.op, ast.Not):
                    return ast.Call(
                        func=ast.Name(id='not', ctx=ast.Load()),
                        args=[node.operand],
                        keywords=[]
                    )
                return node
        
        # Apply the transformer to the AST
        transformed_tree = LogicalTransformer().visit(tree)
        
        # Compile and evaluate the transformed expression
        code = compile(ast.fix_missing_locations(transformed_tree), '<string>', 'eval')
        result = eval(code)
        
        # Ensure the result is a boolean
        return bool(result)
    
    except Exception as e:
        # Return False if evaluation fails
        return False

# Test the function
if __name__ == "__main__":
    print(tentacle('True and False'))  # Should print: False
    print(tentacle('not (True or False)'))  # Should print: False
    print(tentacle('True and (False or True)'))  # Should print: True
    print(tentacle('not True and False'))  # Should print: False
    print(tentacle('True or not False'))  # Should print: True
    print(tentacle('not (not True and not False)'))  # Should print: True
    print(tentacle('invalid expression'))  # Should print: False