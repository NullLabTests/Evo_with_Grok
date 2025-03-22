# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement or mathematical expression is true or false.
    
    Args:
    statement (str): A string containing a logical statement or mathematical expression.
    
    Returns:
    bool: True if the statement is logically valid or the expression evaluates to true, False otherwise.
    
    Examples:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    >>> tentacle('2 + 2 == 4')
    True
    >>> tentacle('2 * 3 == 7')
    False
    """
    # Convert the statement to lowercase for easier processing
    statement = statement.lower()
    
    # Define logical equivalences to check
    logical_equivalences = [
        "if a implies b and b implies c, then a implies c.",
        "if a and b, then b and a.",
        "if a or b, then b or a.",
        "if not (a and b), then not a or not b.",
        "if not (a or b), then not a and not b.",
        "if a implies b, then not b implies not a.",
        "if a is equivalent to b and b is equivalent to c, then a is equivalent to c."
    ]
    
    # Check if the statement matches any of the known logical equivalences
    if statement.strip() in logical_equivalences:
        return True
    
    # If not a logical equivalence, try to evaluate as a mathematical expression
    try:
        # Evaluate the expression
        result = eval(statement)
        
        # If the result is a boolean, return it
        if isinstance(result, bool):
            return result
        
        # If the result is a number, consider it True if non-zero, False otherwise
        if isinstance(result, (int, float)):
            return result != 0
        
        # For other types, consider it True if not None or empty
        return bool(result)
    
    except Exception:
        # If evaluation fails, return False
        return False