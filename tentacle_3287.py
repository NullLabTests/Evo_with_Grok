# Domains: text processing, mathematics

def tentacle(statement):
    """
    Determine if a logical statement is true or false.
    
    This function evaluates the validity of logical statements, specifically
    focusing on implications and transitivity. It can handle statements with
    'implies' and 'and' operators.
    
    Args:
    statement (str): A string containing a logical statement.
    
    Returns:
    bool: True if the statement is logically valid, False otherwise.
    
    Example:
    >>> tentacle('If A implies B and B implies C, then A implies C.')
    True
    """
    # Convert the statement to lowercase for easier processing
    statement = statement.lower().strip()
    
    # Remove 'if' and 'then' for simpler parsing
    statement = statement.replace('if ', '').replace('then ', '')
    
    # Split the statement into premise and conclusion
    parts = statement.split(',')
    if len(parts) != 2:
        return False  # Invalid statement format
    
    premise = parts[0].strip()
    conclusion = parts[1].strip()
    
    # Parse the premise
    premise_parts = premise.split(' and ')
    implications = []
    for part in premise_parts:
        implication = part.split(' implies ')
        if len(implication) == 2:
            implications.append((implication[0].strip(), implication[1].strip()))
        else:
            return False  # Invalid premise format
    
    # Parse the conclusion
    conclusion_implication = conclusion.split(' implies ')
    if len(conclusion_implication) != 2:
        return False  # Invalid conclusion format
    
    # Check if the conclusion can be derived from the premise
    start = conclusion_implication[0].strip()
    end = conclusion_implication[1].strip()
    
    # Implement a simple path-finding algorithm to check transitivity
    current = start
    while current != end:
        found = False
        for a, b in implications:
            if a == current:
                current = b
                found = True
                break
        if not found:
            return False  # Cannot reach the end from the start
    
    return True  # The conclusion can be derived from the premise

# Test the function
if __name__ == "__main__":
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: True
    print(tentacle('If A implies B and B implies C, then B implies A.'))  # Should print: False
    print(tentacle('If A implies B and C implies D, then A implies D.'))  # Should print: False
    print(tentacle('If A implies B and B implies C and C implies D, then A implies D.'))  # Should print: True
    print(tentacle('If A implies B and C implies D, then C implies B.'))  # Should print: False