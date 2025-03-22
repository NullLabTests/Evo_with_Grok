# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers provided as a string.

    Args:
    numbers (str): A string of comma-separated numbers.

    Returns:
    str: A string of sorted numbers in ascending order, separated by commas.

    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    # Split the input string into a list of strings
    number_list = numbers.split(',')
    
    # Convert each string to a float for proper numerical sorting
    number_list = [float(num) for num in number_list]
    
    # Sort the list of numbers
    sorted_numbers = sorted(number_list)
    
    # Convert the sorted numbers back to strings and join them with commas
    result = ','.join(str(num) for num in sorted_numbers)
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('5.5,2.1,8.9,1.0'))  # Should print: '1.0,2.1,5.5,8.9'
    print(tentacle('10,9,8,7,6,5,4,3,2,1'))  # Should print: '1,2,3,4,5,6,7,8,9,10'