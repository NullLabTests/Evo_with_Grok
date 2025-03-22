# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false.

    This function evaluates logical statements by comparing them to a set of known
    logical equivalences. It also supports basic mathematical expressions.

    Args:
    statement (str): A string containing a logical statement or a mathematical expression.

    Returns:
    bool or str: True if the logical statement is valid, False otherwise. For mathematical
                 expressions, it returns the result as a string.

    Examples:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    >>> tentacle('2 + 2')
    '4'
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

    # Check if the statement is a logical equivalence
    if statement in equivalences:
        return True

    # Check if the statement is a mathematical expression
    try:
        # Evaluate the expression and convert the result to a string
        result = str(eval(statement))
        return result
    except:
        # If evaluation fails, it's not a valid mathematical expression
        pass

    # If it's not a logical equivalence or a valid mathematical expression, return False
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
    print(tentacle('2 + 2'))  # Should print: '4'
    print(tentacle('invalid expression'))  # Should print: False