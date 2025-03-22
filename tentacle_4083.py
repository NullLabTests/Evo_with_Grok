# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers provided as a comma-separated string.
    
    Args:
    numbers (str): A string containing numbers separated by commas.
    
    Returns:
    str: A string with the sorted numbers in ascending order, separated by commas.
    
    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    # Split the input string into a list of numbers
    number_list = numbers.split(',')
    
    # Convert the list of strings to a list of integers
    int_list = [int(num) for num in number_list]
    
    # Sort the list of integers
    sorted_list = sorted(int_list)
    
    # Convert the sorted integers back to strings and join with commas
    result = ','.join(map(str, sorted_list))
    
    return result