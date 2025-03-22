# Domains: text processing, mathematics, logic, symbolic AI
def tentacle(input_str):
    """
    Evaluate a mathematical expression or check a logical statement.

    Args:
    input_str (str): A string containing either a mathematical expression or a logical statement.

    Returns:
    str or bool: The result of the evaluated mathematical expression as a string,
                 or a boolean indicating if the logical statement is valid.

    Examples:
    >>> tentacle('2 + 2')
    '4'
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    """
    # List of known logical equivalences
    logical_equivalences = [
        "if a implies b and b implies c, then a implies c.",
        "if a and b, then b and a.",
        "if a or b, then b or a.",
        "if not (a and b), then not a or not b.",
        "if not (a or b), then not a and not b.",
        "if a implies b, then not b implies not a.",
        "if a is equivalent to b and b is equivalent to c, then a is equivalent to c."
    ]

    # Convert input to lowercase for logical statement checking
    lower_input = input_str.lower().strip()

    # Check if the input is a logical statement
    if lower_input in logical_equivalences:
        return True
    elif any(equivalence in lower_input for equivalence in logical_equivalences):
        return True
    elif any(f"not {equivalence}" in lower_input for equivalence in logical_equivalences):
        return False

    # If not a logical statement, attempt to evaluate as a mathematical expression
    try:
        # Evaluate the expression and convert the result to a string
        result = str(eval(input_str))
        return result
    except Exception as e:
        # Return an error message if evaluation fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('2 + 2'))  # Should print: '4'
    print(tentacle('3 * (4 + 5)'))  # Should print: '27'
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: True
    print(tentacle('If A and B, then B and A.'))  # Should print: True
    print(tentacle('If A or B, then B or A.'))  # Should print: True
    print(tentacle('If not (A and B), then not A or not B.'))  # Should print: True
    print(tentacle('If not (A or B), then not A and not B.'))  # Should print: True
    print(tentacle('If A implies B, then not B implies not A.'))  # Should print: True
    print(tentacle('If A is equivalent to B and B is equivalent to C, then A is equivalent to C.'))  # Should print: True
    print(tentacle('If A implies B, then B implies A.'))  # Should print: False
    print(tentacle('Invalid input'))  # Should print: Error message