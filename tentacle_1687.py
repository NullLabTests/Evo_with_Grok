# Domains: text processing, mathematics
def tentacle(numbers_str):
    """
    Sort a list of numbers provided as a string.

    Args:
    numbers_str (str): A string containing comma-separated numbers.

    Returns:
    str: A string of sorted numbers in ascending order, separated by commas.

    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    # Split the input string into a list of numbers
    numbers_list = numbers_str.split(',')
    
    # Convert the list of strings to a list of integers
    numbers = [int(num) for num in numbers_list]
    
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Convert the sorted numbers back to strings and join them with commas
    result = ','.join(map(str, sorted_numbers))
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('9,5,7,1,3'))  # Should print: '1,3,5,7,9'
    print(tentacle('10,8,6,4,2'))  # Should print: '2,4,6,8,10'