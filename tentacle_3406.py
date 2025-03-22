# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers given as a string.

    Args:
    numbers (str): A string containing numbers separated by commas.

    Returns:
    str: A string containing the sorted numbers separated by commas.

    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    # Split the input string into a list of numbers
    number_list = numbers.split(',')
    
    # Convert each number to an integer
    number_list = [int(num) for num in number_list]
    
    # Sort the list of numbers
    sorted_list = sorted(number_list)
    
    # Convert the sorted numbers back to strings and join them
    result = ','.join(str(num) for num in sorted_list)
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('9,5,7,1,3'))  # Should print: '1,3,5,7,9'
    print(tentacle('10,20,5,15'))  # Should print: '5,10,15,20'