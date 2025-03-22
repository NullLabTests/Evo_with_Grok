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
    num_list = numbers.split(',')
    
    # Convert the list of string numbers to a list of integers
    num_list = [int(num) for num in num_list]
    
    # Sort the list of numbers in ascending order
    num_list.sort()
    
    # Convert the sorted list back to a string of comma-separated numbers
    sorted_numbers = ','.join(map(str, num_list))
    
    return sorted_numbers

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('9,5,7,1,3'))  # Should print: '1,3,5,7,9'
    print(tentacle('10,2,8,6,4'))  # Should print: '2,4,6,8,10'