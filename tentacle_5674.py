# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers given as a string.

    Args:
    numbers (str): A string containing comma-separated numbers.

    Returns:
    str: A string containing the sorted numbers, comma-separated.

    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    # Split the input string into a list of numbers
    number_list = numbers.split(',')

    # Convert the list of strings to a list of integers
    number_list = [int(num) for num in number_list]

    # Sort the list of numbers
    sorted_numbers = sorted(number_list)

    # Convert the sorted numbers back to strings and join them
    result = ','.join(map(str, sorted_numbers))

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('5,2,8,1,9'))  # Should print: '1,2,5,8,9'
    print(tentacle('10,3,7,1'))  # Should print: '1,3,7,10'