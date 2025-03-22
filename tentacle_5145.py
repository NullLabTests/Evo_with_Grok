# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers given as a string.

    Args:
    numbers (str): A string containing comma-separated numbers.

    Returns:
    str: A string containing the sorted numbers in ascending order, comma-separated.

    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    # Split the input string into a list of numbers
    num_list = numbers.split(',')

    # Convert the list of strings to a list of floats
    num_list = [float(num) for num in num_list]

    # Sort the list of numbers
    num_list.sort()

    # Convert the sorted list back to strings and join with commas
    sorted_numbers = ','.join(str(num) for num in num_list)

    return sorted_numbers

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('5.5,2.1,8.9,3.7'))  # Should print: '2.1,3.7,5.5,8.9'
    print(tentacle('-1,0,1'))  # Should print: '-1,0,1'