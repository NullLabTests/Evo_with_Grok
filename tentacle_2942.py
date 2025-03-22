# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers given as a string.

    Args:
    numbers (str): A string containing numbers separated by commas.

    Returns:
    str: A string containing the sorted numbers separated by commas.

    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    try:
        # Split the input string into a list of numbers
        number_list = [int(num.strip()) for num in numbers.split(',')]
        
        # Sort the list of numbers
        sorted_list = sorted(number_list)
        
        # Convert the sorted list back to a string
        result = ','.join(map(str, sorted_list))
        
        return result
    except ValueError:
        # Return an error message if input is not valid
        return "Error: Invalid input. Please provide a list of numbers separated by commas."

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('5,2,8,1,9'))  # Should print: '1,2,5,8,9'
    print(tentacle('10,3,7,1'))  # Should print: '1,3,7,10'
    print(tentacle(''))  # Should print: ''
    print(tentacle('a,b,c'))  # Should print: 'Error: Invalid input. Please provide a list of numbers separated by commas.'