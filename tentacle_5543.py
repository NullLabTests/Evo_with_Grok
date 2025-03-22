# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers given as a string.
    
    Args:
    numbers (str): A string containing comma-separated numbers.
    
    Returns:
    str: A string of sorted numbers separated by commas.
    
    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    # Split the input string into a list of numbers
    num_list = [float(num.strip()) for num in numbers.split(',')]
    
    # Sort the list of numbers
    sorted_list = sorted(num_list)
    
    # Convert the sorted list back to a string
    result = ','.join(str(num) for num in sorted_list)
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('5.5,2.1,8.9,3.7'))  # Should print: '2.1,3.7,5.5,8.9'
    print(tentacle('-1,0,1,-2'))  # Should print: '-2,-1,0,1'