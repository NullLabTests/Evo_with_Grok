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
    num_list = numbers.split(',')

    # Convert the list of string numbers to a list of integers
    int_list = [int(num) for num in num_list]

    # Sort the list of integers
    sorted_list = sorted(int_list)

    # Convert the sorted list back to strings and join with commas
    result = ','.join(str(num) for num in sorted_list)

    return result

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('5,2,8,1,9'))  # Should print: '1,2,5,8,9'
    print(tentacle('10,5,3,7'))  # Should print: '3,5,7,10'