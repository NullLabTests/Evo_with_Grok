# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers provided as a string.
    
    Args:
    numbers (str): A string containing comma-separated numbers.
    
    Returns:
    str: A string containing the sorted numbers in ascending order, separated by commas.
    
    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    try:
        # Split the input string into a list of numbers
        number_list = [float(num.strip()) for num in numbers.split(',')]
        
        # Sort the list of numbers
        sorted_numbers = sorted(number_list)
        
        # Convert the sorted numbers back to a string
        result = ','.join(str(num) for num in sorted_numbers)
        
        return result
    except ValueError:
        # Return an error message if the input is not valid
        return "Error: Invalid input. Please provide comma-separated numbers."

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('5.5,2.1,3.7,1.2'))  # Should print: '1.2,2.1,3.7,5.5'
    print(tentacle('10,9,8,7,6,5,4,3,2,1'))  # Should print: '1,2,3,4,5,6,7,8,9,10'
    print(tentacle('invalid input'))  # Should print: 'Error: Invalid input. Please provide comma-separated numbers.'