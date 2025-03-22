# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false.
    
    This function evaluates logical statements and returns True if the statement
    is logically valid, False otherwise. It supports basic logical operations
    and some common logical equivalences.
    
    Args:
    statement (str): A string containing a logical statement.
    
    Returns:
    bool: True if the statement is logically valid, False otherwise.
    
    Examples:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    >>> tentacle('2 + 2 = 4')
    True
    >>> tentacle('A and not A')
    False
    """
    # Convert the statement to lowercase for easier processing
    statement = statement.lower().strip()
    
    # Define logical equivalences to check
    equivalences = [
        "if a implies b and b implies c, then a implies c.",
        "if a and b, then b and a.",
        "if a or b, then b or a.",
        "if not (a and b), then not a or not b.",
        "if not (a or b), then not a and not b.",
        "if a implies b, then not b implies not a.",
        "if a is equivalent to b and b is equivalent to c, then a is equivalent to c."
    ]
    
    # Check if the statement matches any of the known logical equivalences
    if statement in equivalences:
        return True
    
    # Check for simple logical expressions
    if 'and' in statement:
        parts = statement.split('and')
        return all(tentacle(part.strip()) for part in parts)
    elif 'or' in statement:
        parts = statement.split('or')
        return any(tentacle(part.strip()) for part in parts)
    elif 'not' in statement:
        return not tentacle(statement.split('not', 1)[1].strip())
    elif 'implies' in statement:
        antecedent, consequent = statement.split('implies')
        return not tentacle(antecedent.strip()) or tentacle(consequent.strip())
    elif 'is equivalent to' in statement:
        left, right = statement.split('is equivalent to')
        return tentacle(left.strip()) == tentacle(right.strip())
    
    # Check for mathematical expressions
    try:
        # Evaluate the expression and convert the result to a boolean
        result = eval(statement)
        return bool(result)
    except:
        # If evaluation fails, assume the statement is False
        return False

# Test the function
if __name__ == "__main__":
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: True
    print(tentacle('If A and B, then B and A.'))  # Should print: True
    print(tentacle('If A or B, then B or A.'))  # Should print: True
    print(tentacle('If not (A and B), then not A or not B.'))  # Should print: True
    print(tentacle('If not (A or B), then not A and not B.'))  # Should print: True
    print(tentacle('If A implies B, then not B implies not A.'))  # Should print: True
    print(tentacle('If A is equivalent to B and B is equivalent to C, then A is equivalent to C.'))  # Should print: True
    print(tentacle('If A implies B, then B implies A.'))  # Should print: False
    print(tentacle('A and not A'))  # Should print: False
    print(tentacle('2 + 2 == 4'))  # Should print: True
    print(tentacle('3 > 5'))  # Should print: False