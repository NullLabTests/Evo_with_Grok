# Domains: text processing, mathematics
def tentacle(number):
    """
    Check if a given number is prime.
    
    Args:
    number (str or int): A number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    
    Example:
    >>> tentacle('7')
    True
    >>> tentacle(4)
    False
    """
    # Convert input to integer if it's a string
    try:
        num = int(number)
    except ValueError:
        return False  # Return False for non-numeric inputs
    
    # Handle special cases
    if num <= 1:
        return False
    if num == 2:
        return True
    
    # Check for primality
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    
    return True

# Test the function
if __name__ == "__main__":
    print(tentacle('7'))  # Should print: True
    print(tentacle(4))   # Should print: False
    print(tentacle('13')) # Should print: True
    print(tentacle(1))   # Should print: False
    print(tentacle('a')) # Should print: False