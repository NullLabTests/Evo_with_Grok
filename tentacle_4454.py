# Domains: text processing, mathematics
def tentacle(numbers_str):
    """
    Sort a list of numbers given as a string.
    
    Args:
    numbers_str (str): A string containing numbers separated by commas.
    
    Returns:
    str: A string with the sorted numbers separated by commas.
    
    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    # Split the input string into a list of numbers
    numbers = numbers_str.split(',')
    
    # Convert the string numbers to integers
    numbers = [int(num) for num in numbers]
    
    # Sort the list of numbers
    numbers.sort()
    
    # Convert the sorted numbers back to strings and join them
    sorted_numbers_str = ','.join(map(str, numbers))
    
    return sorted_numbers_str

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('5,2,8,1,9'))  # Should print: '1,2,5,8,9'
    print(tentacle('10,5,20,15'))  # Should print: '5,10,15,20'