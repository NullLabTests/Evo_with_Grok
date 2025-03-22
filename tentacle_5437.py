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
    try:
        # Convert input to integer
        num = int(number)
        
        # Handle edge cases
        if num < 2:
            return False
        
        # Check for primality
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    except ValueError:
        # Return False if input cannot be converted to an integer
        return False

# Test the function
if __name__ == "__main__":
    print(tentacle('7'))  # Should print: True
    print(tentacle(10))  # Should print: False
    print(tentacle('1'))  # Should print: False
    print(tentacle('17'))  # Should print: True
    print(tentacle('hello'))  # Should print: False