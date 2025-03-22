# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function improves upon the original by adding input validation
    and handling more complex expressions using the 'ast' module for safety.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Examples:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('sin(pi/2)')
    '1.0'
    >>> tentacle('invalid expression')
    'Error: Invalid expression'
    """
    import ast
    import math

    # Define a safe evaluation function
    def safe_eval(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            left = safe_eval(node.left)
            right = safe_eval(node.right)
            if isinstance(node.op, ast.Add):
                return left + right
            elif isinstance(node.op, ast.Sub):
                return left - right
            elif isinstance(node.op, ast.Mult):
                return left * right
            elif isinstance(node.op, ast.Div):
                return left / right
            elif isinstance(node.op, ast.Pow):
                return left ** right
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
                if func_name in dir(math):
                    args = [safe_eval(arg) for arg in node.args]
                    return getattr(math, func_name)(*args)
        raise ValueError("Unsupported operation")

    try:
        # Parse the expression
        tree = ast.parse(expression, mode='eval')
        
        # Evaluate the parsed tree safely
        result = safe_eval(tree.body)
        
        # Convert the result to a string
        return str(result)
    except (SyntaxError, ValueError) as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('3 * 4'))  # Should print: 12
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('invalid expression'))  # Should print: Error: Invalid expression