# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers provided as a string.
    
    Args:
    numbers (str): A string of comma-separated numbers.
    
    Returns:
    str: A string of sorted numbers, comma-separated.
    
    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    # Split the input string into a list of numbers
    num_list = numbers.split(',')
    
    # Convert the strings to integers, sort them, and convert back to strings
    sorted_nums = sorted(map(int, num_list))
    sorted_nums = map(str, sorted_nums)
    
    # Join the sorted numbers back into a comma-separated string
    return ','.join(sorted_nums)

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('9,5,7,1,3'))  # Should print: '1,3,5,7,9'
    print(tentacle('10,20,5,15'))  # Should print: '5,10,15,20'