# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false.

    This function combines mathematical evaluation with logical statement validation.
    It first attempts to evaluate the statement as a mathematical expression, and if that fails,
    it checks the statement against a list of known logical equivalences.

    Args:
    statement (str): A string containing a logical or mathematical statement.

    Returns:
    bool: True if the statement is logically valid or mathematically true, False otherwise.

    Examples:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    >>> tentacle('2 + 2 == 4')
    True
    >>> tentacle('2 + 2 == 5')
    False
    """
    # First, attempt to evaluate the statement as a mathematical expression
    try:
        result = eval(statement)
        return bool(result)
    except:
        # If evaluation fails, treat the statement as a logical statement
        statement = statement.lower()
        
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
        return statement.strip() in equivalences

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
    print(tentacle('2 + 2 == 4'))  # Should print: True
    print(tentacle('2 + 2 == 5'))  # Should print: False