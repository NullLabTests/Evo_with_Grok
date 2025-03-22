# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers provided as a string.

    Args:
    numbers (str): A string containing numbers separated by commas.

    Returns:
    str: A string with the sorted numbers separated by commas.

    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    # Split the input string into a list of numbers
    number_list = numbers.split(',')
    
    # Convert the string numbers to integers
    int_list = [int(num) for num in number_list]
    
    # Sort the list of integers
    sorted_list = sorted(int_list)
    
    # Convert the sorted integers back to strings and join them
    sorted_numbers = ','.join(map(str, sorted_list))
    
    return sorted_numbers

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('5,2,8,1,9'))  # Should print: '1,2,5,8,9'