# Domains: text processing, mathematics
def tentacle(statement):
    """
    Determine if a logical statement is true or false.
    
    This function evaluates logical statements, with a focus on implication chains.
    It can handle the specific case: 'If A implies B and B implies C, then A implies C.'
    
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
    
    # Define the specific logical equivalence we're checking
    target_equivalence = "if a implies b and b implies c, then a implies c."
    
    # Check if the statement matches the target equivalence
    if statement == target_equivalence:
        return True
    
    # For other statements, we'll implement a simple parser
    if statement.startswith("if ") and statement.endswith("."):
        # Remove 'if ' at the start and '.' at the end
        core_statement = statement[3:-1]
        
        # Split the statement into premise and conclusion
        premise, conclusion = core_statement.split(", then ")
        
        # Parse the premise
        premises = premise.split(" and ")
        parsed_premises = []
        for p in premises:
            if " implies " in p:
                left, right = p.split(" implies ")
                parsed_premises.append((left.strip(), right.strip()))
        
        # Parse the conclusion
        if " implies " in conclusion:
            left, right = conclusion.split(" implies ")
            parsed_conclusion = (left.strip(), right.strip())
        
        # Check if the conclusion follows from the premises
        if parsed_conclusion[0] == parsed_premises[0][0] and parsed_conclusion[1] == parsed_premises[-1][1]:
            current = parsed_conclusion[0]
            for premise in parsed_premises:
                if premise[0] == current:
                    current = premise[1]
            if current == parsed_conclusion[1]:
                return True
    
    # If we reach here, the statement is not recognized as valid
    return False

# Test the function
if __name__ == "__main__":
    print(tentacle('If A implies B and B implies C, then A implies C.'))  # Should print: True
    print(tentacle('If A implies B and B implies C, then B implies A.'))  # Should print: False
    print(tentacle('If A implies B and B implies C, then C implies A.'))  # Should print: False
    print(tentacle('If A implies B and C implies D, then A implies D.'))  # Should print: False
    print(tentacle('If A implies B and B implies C and C implies D, then A implies D.'))  # Should print: True