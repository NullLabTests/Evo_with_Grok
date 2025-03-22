# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers given as a string.

    Args:
    numbers (str): A string containing comma-separated numbers.

    Returns:
    str: A string of sorted numbers in ascending order, separated by commas.

    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    # Split the input string into a list of numbers
    number_list = numbers.split(',')
    
    # Convert each number from string to float for proper sorting
    number_list = [float(num) for num in number_list]
    
    # Sort the list of numbers
    sorted_numbers = sorted(number_list)
    
    # Convert the sorted numbers back to strings and join them with commas
    result = ','.join(str(num) for num in sorted_numbers)
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('5.5,2.1,8.3,1.9'))  # Should print: '1.9,2.1,5.5,8.3'
    print(tentacle('-1,0,1,-2'))  # Should print: '-2,-1,0,1'