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
    try:
        # Split the input string into a list of numbers
        num_list = [int(num.strip()) for num in numbers.split(',')]
        
        # Sort the list of numbers
        sorted_list = sorted(num_list)
        
        # Convert the sorted list back to a string
        result = ','.join(map(str, sorted_list))
        
        return result
    except ValueError:
        # Return an error message if the input is not valid
        return "Error: Invalid input. Please provide comma-separated numbers."

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('10,5,8,3,1'))  # Should print: '1,3,5,8,10'
    print(tentacle(''))  # Should print: ''
    print(tentacle('a,b,c'))  # Should print: 'Error: Invalid input. Please provide comma-separated numbers.'