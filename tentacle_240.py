# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Find the maximum value in a list of numbers given as a string.
    
    Args:
    numbers (str): A string containing a list of numbers, e.g., '[3,1,4,2]'.
    
    Returns:
    str: The maximum value in the list as a string.
    
    Example:
    >>> tentacle('[3,1,4,2]')
    '4'
    """
    # Remove brackets and split the string into a list of number strings
    num_list = numbers.strip('[]').split(',')
    
    # Convert the list of number strings to a list of integers
    int_list = [int(num) for num in num_list]
    
    # Find the maximum value in the list
    max_value = max(int_list)
    
    # Convert the maximum value to a string and return it
    return str(max_value)

# Test the function
if __name__ == "__main__":
    print(tentacle('[3,1,4,2]'))  # Should print: 4
    print(tentacle('[10,5,8,12,3]'))  # Should print: 12
    print(tentacle('[-5,-2,-8,-1]'))  # Should print: -1