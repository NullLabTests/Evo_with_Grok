# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Find the maximum value in a list of numbers given as a string.
    
    Args:
    numbers (str): A string containing a list of numbers, e.g., '[3,1,4,2]'.
    
    Returns:
    str: The maximum value in the list as a string.
    
    Example:
    >>> tentacle('[3,1,4,2]')
    '4'
    """
    try:
        # Convert the string to a list of numbers
        num_list = eval(numbers)
        
        # Check if the list contains only numbers
        if all(isinstance(num, (int, float)) for num in num_list):
            # Find and return the maximum value as a string
            return str(max(num_list))
        else:
            return "Error: List contains non-numeric values"
    except Exception as e:
        # Return an error message if processing fails
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('[3,1,4,2]'))  # Should print: 4
    print(tentacle('[10, -5, 0, 7.5]'))  # Should print: 10
    print(tentacle('[3, "a", 4]'))  # Should print: Error: List contains non-numeric values
    print(tentacle('invalid input'))  # Should print: Error: invalid input