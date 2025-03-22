# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers provided as a string.

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
    
    # Convert the strings to integers, sort them, and convert back to strings
    sorted_numbers = sorted(map(int, number_list))
    sorted_numbers = map(str, sorted_numbers)
    
    # Join the sorted numbers back into a string
    return ','.join(sorted_numbers)

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('9,5,7,1,3'))  # Should print: '1,3,5,7,9'
    print(tentacle('10,2,8,6,4'))  # Should print: '2,4,6,8,10'