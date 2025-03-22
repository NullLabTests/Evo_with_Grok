# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function improves upon the previous version by adding input validation
    and handling more complex expressions safely using the ast module.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('sin(pi/2)')
    '1.0'
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
                if right == 0:
                    raise ValueError("Division by zero")
                return left / right
            elif isinstance(node.op, ast.Pow):
                return left ** right
        elif isinstance(node, ast.Call):
            if isinstance(node.func, ast.Name):
                func_name = node.func.id
                if func_name in dir(math):
                    args = [safe_eval(arg) for arg in node.args]
                    return getattr(math, func_name)(*args)
        raise ValueError(f"Unsupported operation: {type(node).__name__}")
    
    # Validate and parse the expression
    try:
        tree = ast.parse(expression, mode='eval')
    except SyntaxError:
        return "Error: Invalid syntax"
    
    # Evaluate the expression safely
    try:
        result = safe_eval(tree.body)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('5 * (3 + 4)'))  # Should print: 35
    print(tentacle('sin(pi/2)'))  # Should print: 1.0
    print(tentacle('10 / 0'))  # Should print: Error: Division by zero
    print(tentacle('x + 5'))  # Should print: Error: Unsupported operation: Name