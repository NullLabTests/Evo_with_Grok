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
    num_list = numbers.split(',')
    
    # Convert the string numbers to integers
    num_list = [int(num) for num in num_list]
    
    # Sort the list of numbers
    num_list.sort()
    
    # Convert the sorted numbers back to strings and join them
    sorted_numbers = ','.join(str(num) for num in num_list)
    
    return sorted_numbers

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('9,5,7,1,3'))  # Should print: '1,3,5,7,9'
    print(tentacle('10,8,6,4,2'))  # Should print: '2,4,6,8,10'