# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function safely evaluates mathematical expressions and returns the result as a string.
    It uses the ast module to parse the expression, which is safer than using eval().
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message if evaluation fails.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    """
    import ast
    import operator
    
    # Define a safe evaluation function
    def safe_eval(node):
        operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
        }
        
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            left = safe_eval(node.left)
            right = safe_eval(node.right)
            op = operators[type(node.op)]
            return op(left, right)
        else:
            raise ValueError(f"Unsupported operation: {type(node)}")
    
    try:
        # Parse the expression
        tree = ast.parse(expression, mode='eval')
        
        # Safely evaluate the parsed expression
        result = safe_eval(tree.body)
        
        # Convert the result to a string and return
        return str(result)
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('3 * 4'))  # Should print: 12
    print(tentacle('10 / 2'))  # Should print: 5.0
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('2 + x'))  # Should print: Error: Unsupported operation: <class '_ast.Name'>