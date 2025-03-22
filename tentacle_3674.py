# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers given as a string.
    
    Args:
    numbers (str): A string containing numbers separated by commas.
    
    Returns:
    str: The sorted numbers as a string, separated by commas.
    
    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    # Split the input string into a list of numbers
    num_list = numbers.split(',')
    
    # Convert the list of strings to a list of integers
    num_list = [int(num) for num in num_list]
    
    # Sort the list of integers
    num_list.sort()
    
    # Convert the sorted list back to a string of comma-separated values
    sorted_numbers = ','.join(map(str, num_list))
    
    return sorted_numbers

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('9,5,7,1,3'))  # Should print: '1,3,5,7,9'
    print(tentacle('10,20,5,15'))  # Should print: '5,10,15,20'