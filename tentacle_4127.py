# Domains: text processing, mathematics
def tentacle(number):
    """
    Check if a given number is prime.
    
    Args:
    number (str): A string representation of a number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    
    Example:
    >>> tentacle('7')
    True
    >>> tentacle('4')
    False
    """
    # Convert the input string to an integer
    try:
        num = int(number)
    except ValueError:
        return False  # Return False if the input is not a valid integer

    # Check for primality
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    # Check odd numbers up to the square root of num
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    
    return True

# Test the function
if __name__ == "__main__":
    print(tentacle('7'))  # Should print: True
    print(tentacle('4'))  # Should print: False
    print(tentacle('1'))  # Should print: False
    print(tentacle('2'))  # Should print: True
    print(tentacle('97'))  # Should print: True
    print(tentacle('100'))  # Should print: False
    print(tentacle('abc'))  # Should print: False