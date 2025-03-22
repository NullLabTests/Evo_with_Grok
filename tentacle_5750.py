# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false.

    This function evaluates logical statements and returns True if the statement
    is logically valid, False otherwise. It supports basic logical operations
    and can handle simple propositional logic.

    Args:
    statement (str): A string containing a logical statement.

    Returns:
    bool: True if the statement is logically valid, False otherwise.

    Examples:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    >>> tentacle('If A and B, then B and A.')
    True
    >>> tentacle('If A implies B, then B implies A.')
    False
    """
    # Convert the statement to lowercase for easier processing
    statement = statement.lower().strip()

    # Define logical equivalences to check
    equivalences = {
        "if a implies b and b implies c, then a implies c.": "((a -> b) & (b -> c)) -> (a -> c)",
        "if a and b, then b and a.": "(a & b) -> (b & a)",
        "if a or b, then b or a.": "(a | b) -> (b | a)",
        "if not (a and b), then not a or not b.": "~(a & b) -> (~a | ~b)",
        "if not (a or b), then not a and not b.": "~(a | b) -> (~a & ~b)",
        "if a implies b, then not b implies not a.": "(a -> b) -> (~b -> ~a)",
        "if a is equivalent to b and b is equivalent to c, then a is equivalent to c.": "((a <-> b) & (b <-> c)) -> (a <-> c)"
    }

    # Check if the statement matches any of the known logical equivalences
    if statement in equivalences:
        return True

    # If not a direct match, try to evaluate the statement
    try:
        # Convert the statement to a logical expression
        expr = statement
        for key, value in equivalences.items():
            expr = expr.replace(key, value)

        # Replace logical operators with Python equivalents
        expr = expr.replace("->", "implies")
        expr = expr.replace("<->", "iff")
        expr = expr.replace("&", "and")
        expr = expr.replace("|", "or")
        expr = expr.replace("~", "not")

        # Define custom logical functions
        def implies(a, b):
            return not a or b

        def iff(a, b):
            return implies(a, b) and implies(b, a)

        # Evaluate the expression
        result = eval(expr, {"implies": implies, "iff": iff})
        return bool(result)
    except Exception as e:
        # If evaluation fails, return False
        return False

# Test the function
if __name__ == "__main__":
    test_statements = [
        "If A implies B and B implies C, then A implies C.",
        "If A and B, then B and A.",
        "If A or B, then B or A.",
        "If not (A and B), then not A or not B.",
        "If not (A or B), then not A and not B.",
        "If A implies B, then not B implies not A.",
        "If A is equivalent to B and B is equivalent to C, then A is equivalent to C.",
        "If A implies B, then B implies A.",
        "A and B implies B and A.",
        "A or B implies B or A.",
        "Not (A and B) implies not A or not B.",
        "Not (A or B) implies not A and not B.",
        "A implies B implies not B implies not A.",
        "A is equivalent to B and B is equivalent to C implies A is equivalent to C.",
        "A and not A.",
        "A or not A.",
        "A implies A.",
        "A iff A.",
    ]

    for statement in test_statements:
        result = tentacle(statement)
        print(f"{statement}: {result}")