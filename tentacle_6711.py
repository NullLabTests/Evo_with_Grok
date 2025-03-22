# Domains: text processing, mathematics
def tentacle(number):
    """
    Check if a given number is prime.
    
    Args:
    number (str or int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    
    Example:
    >>> tentacle('7')
    True
    >>> tentacle(10)
    False
    """
    # Convert input to integer if it's a string
    try:
        num = int(number)
    except ValueError:
        return False  # Return False for non-numeric inputs

    # Handle special cases
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    # Check for primality
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

# Test the function
if __name__ == "__main__":
    print(tentacle('7'))  # Should print: True
    print(tentacle(10))  # Should print: False
    print(tentacle('13'))  # Should print: True
    print(tentacle(1))  # Should print: False
    print(tentacle('2'))  # Should print: True
    print(tentacle('4'))  # Should print: False
    print(tentacle('97'))  # Should print: True
    print(tentacle('100'))  # Should print: False