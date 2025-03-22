# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function improves upon previous tentacles by:
    - Using a safer evaluation method (ast.literal_eval) for basic expressions.
    - Implementing a custom evaluator for more complex expressions.
    - Providing more detailed error messages.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Examples:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('3 * (4 + 5)')
    '27'
    """
    import ast
    import operator
    
    # Dictionary of allowed operators
    ops = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.Pow: operator.pow
    }
    
    def eval_expr(node):
        if isinstance(node, ast.Num):
            return node.n
        elif isinstance(node, ast.BinOp):
            return ops[type(node.op)](eval_expr(node.left), eval_expr(node.right))
        else:
            raise ValueError(f"Unsupported operation: {type(node)}")
    
    try:
        # Try to evaluate using ast.literal_eval for simple expressions
        result = ast.literal_eval(expression)
        return str(result)
    except ValueError:
        # If that fails, try our custom evaluator
        try:
            tree = ast.parse(expression, mode='eval').body
            result = eval_expr(tree)
            return str(result)
        except Exception as e:
            # Return a detailed error message if evaluation fails
            return f"Error: Invalid expression - {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('3 * (4 + 5)'))  # Should print: 27
    print(tentacle('10 / 2'))  # Should print: 5.0
    print(tentacle('2 ** 3'))  # Should print: 8
    print(tentacle('invalid expression'))  # Should print an error message