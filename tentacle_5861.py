# Domains: text processing, mathematics
def tentacle(numbers_str):
    """
    Sort a list of numbers given as a comma-separated string.
    
    Args:
    numbers_str (str): A string containing numbers separated by commas.
    
    Returns:
    str: A string containing the sorted numbers in ascending order, separated by commas.
    
    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    # Split the input string into a list of numbers
    numbers = numbers_str.split(',')
    
    # Convert the list of strings to a list of integers
    try:
        numbers = [int(num) for num in numbers]
    except ValueError:
        return "Error: Invalid input. Please provide only integers separated by commas."
    
    # Sort the list of numbers
    sorted_numbers = sorted(numbers)
    
    # Convert the sorted list back to a comma-separated string
    result = ','.join(map(str, sorted_numbers))
    
    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('5,2,8,1,9'))  # Should print: '1,2,5,8,9'
    print(tentacle('10,5,3,7'))  # Should print: '3,5,7,10'
    print(tentacle('1,1,1,2,2'))  # Should print: '1,1,1,2,2'
    print(tentacle(''))  # Should print: ''
    print(tentacle('a,b,c'))  # Should print: Error message