# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers provided as a string.

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
    
    # Convert each number from string to float for proper sorting
    num_list = [float(num) for num in num_list]
    
    # Sort the list of numbers in ascending order
    num_list.sort()
    
    # Convert each number back to string and join them with commas
    sorted_numbers = ','.join(map(str, num_list))
    
    return sorted_numbers

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('5.5,2.1,8.9,3.7'))  # Should print: '2.1,3.7,5.5,8.9'
    print(tentacle('10,9,8,7,6,5,4,3,2,1'))  # Should print: '1,2,3,4,5,6,7,8,9,10'