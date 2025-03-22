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
            # Find the maximum value
            max_value = max(num_list)
            return str(max_value)
        else:
            return "Error: List must contain only numbers."
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('[3,1,4,2]'))  # Should print: 4
    print(tentacle('[5.5, 2, -1, 10]'))  # Should print: 10
    print(tentacle('[-3, -1, -5, -2]'))  # Should print: -1
    print(tentacle('[1, "two", 3]'))  # Should print: Error: List must contain only numbers.
    print(tentacle('invalid input'))  # Should print: Error: ...