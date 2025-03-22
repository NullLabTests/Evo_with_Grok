# Domains: text processing, mathematics
def tentacle(number):
    """
    Check if a given number is prime.
    
    Args:
    number (int): The number to check for primality.
    
    Returns:
    bool: True if the number is prime, False otherwise.
    
    Example:
    >>> tentacle(7)
    True
    >>> tentacle(4)
    False
    """
    # Convert the input to an integer to ensure proper processing
    try:
        number = int(number)
    except ValueError:
        return False  # Return False for non-integer inputs

    # Check if the number is less than 2 (not prime)
    if number < 2:
        return False

    # Check for divisibility from 2 to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False

    # If no divisors found, the number is prime
    return True

# Test the function
if __name__ == "__main__":
    print(tentacle(7))  # Should print: True
    print(tentacle(4))  # Should print: False
    print(tentacle(17))  # Should print: True
    print(tentacle(100))  # Should print: False
    print(tentacle("13"))  # Should print: True
    print(tentacle("25"))  # Should print: False
    print(tentacle("0"))  # Should print: False
    print(tentacle("-5"))  # Should print: False