# Domains: text processing, mathematics
def tentacle(expression):
    """
    Evaluate a mathematical expression given as a string.
    
    This function improves upon the previous version by:
    - Adding support for more complex expressions
    - Improving error handling and reporting
    - Implementing a simple tokenizer for better expression parsing
    
    Args:
    expression (str): A string containing a mathematical expression.
    
    Returns:
    str: The result of the evaluated expression as a string, or an error message.
    
    Example:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('(3 * 4) + (5 / 2)')
    '14.5'
    """
    def tokenize(expr):
        """Simple tokenizer to split the expression into tokens."""
        tokens = []
        current = ''
        for char in expr:
            if char in '+-*/()':
                if current:
                    tokens.append(current)
                    current = ''
                tokens.append(char)
            else:
                current += char
        if current:
            tokens.append(current)
        return tokens

    try:
        # Tokenize the expression
        tokens = tokenize(expression)
        
        # Reconstruct the expression from tokens
        reconstructed = ''.join(tokens)
        
        # Evaluate the expression
        result = eval(reconstructed)
        
        # Convert the result to a string and return
        return str(result)
    except ZeroDivisionError:
        return "Error: Division by zero"
    except SyntaxError:
        return "Error: Invalid syntax"
    except NameError:
        return "Error: Undefined variable"
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: 4
    print(tentacle('(3 * 4) + (5 / 2)'))  # Should print: 14.5
    print(tentacle('10 / 0'))  # Should print: Error: Division by zero
    print(tentacle('2 +'))  # Should print: Error: Invalid syntax
    print(tentacle('x + 2'))  # Should print: Error: Undefined variable
    print(tentacle('2 ** 3'))  # Should print: 8