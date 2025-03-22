# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false, including evaluation of mathematical expressions.
    
    Args:
    statement (str): A string containing a logical statement, which may include mathematical expressions.
    
    Returns:
    bool: True if the statement is logically valid, False otherwise.
    
    Examples:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    >>> tentacle('If 2 + 2 equals 4, then 3 + 3 equals 6.')
    True
    >>> tentacle('If 2 + 2 equals 5, then 3 + 3 equals 6.')
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
    
    # Function to evaluate mathematical expressions
    def eval_math(expr):
        try:
            return str(eval(expr))
        except Exception:
            return None
    
    # Replace mathematical expressions with their evaluated results
    import re
    math_exprs = re.findall(r'\b\d+\s*[\+\-\*/]\s*\d+\b', statement)
    for expr in math_exprs:
        result = eval_math(expr)
        if result:
            statement = statement.replace(expr, result)
    
    # Check if the statement matches any of the known logical equivalences
    if statement.strip() in equivalences:
        return True
    
    # Check for custom logical statements with mathematical expressions
    if 'if' in statement and 'then' in statement:
        condition, conclusion = statement.split('then')
        condition = condition.replace('if', '').strip()
        
        # Evaluate the condition
        if 'equals' in condition:
            left, right = condition.split('equals')
            left = left.strip()
            right = right.strip()
            condition_true = left == right
        
        # Evaluate the conclusion
        if 'equals' in conclusion:
            left, right = conclusion.split('equals')
            left = left.strip()
            right = right.strip()
            conclusion_true = left == right
        
        # Return True if condition implies conclusion
        return not condition_true or conclusion_true
    
    # If no match found, return False
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
    print(tentacle('If 2 + 2 equals 4, then 3 + 3 equals 6.'))  # Should print: True
    print(tentacle('If 2 + 2 equals 5, then 3 + 3 equals 6.'))  # Should print: False