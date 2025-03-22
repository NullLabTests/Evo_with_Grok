# Domains: text processing, mathematics
def tentacle(numbers_str):
    """
    Sort a list of numbers provided as a string.
    
    Args:
    numbers_str (str): A string of comma-separated numbers.
    
    Returns:
    str: A string of sorted numbers separated by commas.
    
    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    # Split the input string into a list of numbers
    numbers = numbers_str.split(',')
    
    # Convert each number from string to float for proper sorting
    numbers = [float(num) for num in numbers]
    
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Convert the sorted numbers back to strings and join them with commas
    result = ','.join(str(num) for num in sorted_numbers)
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('5.5,2.1,8.9,3.0'))  # Should print: '2.1,3.0,5.5,8.9'
    print(tentacle('10,9,8,7,6,5,4,3,2,1'))  # Should print: '1,2,3,4,5,6,7,8,9,10'