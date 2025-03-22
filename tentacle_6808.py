# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Sort a list of numbers given as a string.
    
    Args:
    numbers (str): A string containing comma-separated numbers.
    
    Returns:
    str: A string of sorted numbers in ascending order, separated by commas.
    
    Example:
    >>> tentacle('3,1,4,2')
    '1,2,3,4'
    """
    try:
        # Split the input string into a list of numbers
        num_list = [float(num.strip()) for num in numbers.split(',')]
        
        # Sort the list of numbers
        sorted_nums = sorted(num_list)
        
        # Convert the sorted numbers back to a string
        result = ','.join(str(num) for num in sorted_nums)
        
        return result
    except ValueError:
        # Return an error message if the input is not valid
        return "Error: Invalid input. Please provide a string of comma-separated numbers."

# Test the function
if __name__ == "__main__":
    print(tentacle('3,1,4,2'))  # Should print: '1,2,3,4'
    print(tentacle('5,2,8,1,9'))  # Should print: '1,2,5,8,9'
    print(tentacle('-1,0,1'))  # Should print: '-1,0,1'
    print(tentacle('3.14,2.71,1.41'))  # Should print: '1.41,2.71,3.14'
    print(tentacle('a,b,c'))  # Should print: 'Error: Invalid input. Please provide a string of comma-separated numbers.'