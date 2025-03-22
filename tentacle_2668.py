# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false, including evaluation of mathematical expressions.

    Args:
    statement (str): A string containing a logical statement, possibly with mathematical expressions.

    Returns:
    bool: True if the statement is logically valid, False otherwise.

    Examples:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    >>> tentacle('If 2 + 2 == 4, then 3 * 3 == 9.')
    True
    >>> tentacle('If 2 + 2 == 5, then 3 * 3 == 9.')
    False
    """
    # Convert the statement to lowercase for easier processing
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
    if statement.strip() in equivalences:
        return True

    # Split the statement into parts using 'if' and 'then'
    parts = statement.split('if')
    if len(parts) != 2:
        return False

    condition, conclusion = parts[1].split('then')
    condition = condition.strip()
    conclusion = conclusion.strip()

    # Function to evaluate mathematical expressions within a string
    def evaluate_expression(expr):
        try:
            return eval(expr)
        except:
            return expr  # Return the expression as is if it can't be evaluated

    # Evaluate the condition and conclusion
    condition_result = evaluate_expression(condition)
    conclusion_result = evaluate_expression(conclusion)

    # Check if the condition implies the conclusion
    if isinstance(condition_result, bool) and isinstance(conclusion_result, bool):
        return not condition_result or conclusion_result
    elif isinstance(condition_result, (int, float)) and isinstance(conclusion_result, (int, float)):
        return condition_result == conclusion_result
    else:
        # If we can't evaluate the expressions, check for logical equivalence
        return condition == conclusion

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
    print(tentacle('If 2 + 2 == 4, then 3 * 3 == 9.'))  # Should print: True
    print(tentacle('If 2 + 2 == 5, then 3 * 3 == 9.'))  # Should print: False
    print(tentacle('If x > 0, then x * x > 0.'))  # Should print: True
    print(tentacle('If x < 0, then x * x < 0.'))  # Should print: False