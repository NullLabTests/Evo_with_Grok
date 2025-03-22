# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers provided as a string.

    Args:
    numbers (str): A string containing comma-separated numbers.

    Returns:
    str: A string with the sorted numbers, also comma-separated.

    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    # Split the input string into a list of numbers
    num_list = numbers.split(',')

    # Convert the strings to integers, sort them, and convert back to strings
    sorted_nums = sorted(map(int, num_list))

    # Join the sorted numbers back into a comma-separated string
    return ','.join(map(str, sorted_nums))

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('5,2,8,1,9'))  # Should print: '1,2,5,8,9'
    print(tentacle('10,3,7,2'))  # Should print: '2,3,7,10'