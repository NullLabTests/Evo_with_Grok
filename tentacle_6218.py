# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function safely evaluates mathematical expressions by using the ast module
    to parse the expression and ensure it only contains valid mathematical operations.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('2 ** 3')
    '8'
    >>> tentacle('1 / 0')
    'Error: division by zero'
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
            try:
                return op(left, right)
            except ZeroDivisionError:
                raise ValueError("division by zero")
        else:
            raise ValueError("Invalid expression")
    
    try:
        # Parse the expression
        tree = ast.parse(expression, mode='eval')
        
        # Evaluate the parsed expression safely
        result = safe_eval(tree.body)
        
        # Convert the result to a string
        return str(result)
    except (SyntaxError, ValueError) as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('1 / 0'))  # Should print: Error: division by zero
    print(tentacle('2 + * 3'))  # Should print: Error: Invalid expression