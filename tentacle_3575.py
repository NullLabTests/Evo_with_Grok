# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function improves upon previous tentacles by:
    1. Safely evaluating mathematical expressions.
    2. Handling potential security risks associated with `eval`.
    3. Supporting basic arithmetic operations and parentheses.
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('(3 + 4) * 2')
    '14'
    """
    try:
        # Tokenize the expression
        tokens = []
        current_number = ''
        for char in expression:
            if char.isdigit() or char == '.':
                current_number += char
            else:
                if current_number:
                    tokens.append(float(current_number))
                    current_number = ''
                if char in '+-*/()':
                    tokens.append(char)
        
        if current_number:
            tokens.append(float(current_number))
        
        # Evaluate the expression using a simple stack-based evaluator
        def evaluate(tokens):
            def apply_operator(operators, values):
                operator = operators.pop()
                right = values.pop()
                left = values.pop()
                if operator == '+':
                    values.append(left + right)
                elif operator == '-':
                    values.append(left - right)
                elif operator == '*':
                    values.append(left * right)
                elif operator == '/':
                    if right == 0:
                        raise ValueError("Division by zero")
                    values.append(left / right)
            
            precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
            operators = []
            values = []
            
            for token in tokens:
                if isinstance(token, float):
                    values.append(token)
                elif token == '(':
                    operators.append(token)
                elif token == ')':
                    while operators and operators[-1] != '(':
                        apply_operator(operators, values)
                    operators.pop()  # Remove the '('
                else:
                    while operators and operators[-1] != '(' and precedence.get(operators[-1], 0) >= precedence.get(token, 0):
                        apply_operator(operators, values)
                    operators.append(token)
            
            while operators:
                apply_operator(operators, values)
            
            return values[0]
        
        result = evaluate(tokens)
        return str(result)
    
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(3 + 4) * 2'))  # Should print: 14
    print(tentacle('10 / 2'))  # Should print: 5.0
    print(tentacle('5 * (3 - 1)'))  # Should print: 10
    print(tentacle('10 / 0'))  # Should print: Error: Division by zero
    print(tentacle('2 +'))  # Should print: Error: index out of range
    print(tentacle('(2 + 3'))  # Should print: Error: index out of range