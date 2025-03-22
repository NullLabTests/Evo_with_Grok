# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Find the maximum value in a list of numbers provided as a string.

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
        
        # Ensure the list contains only numbers
        if all(isinstance(num, (int, float)) for num in num_list):
            # Find the maximum value in the list
            max_value = max(num_list)
            return str(max_value)
        else:
            return "Error: List must contain only numbers."
    except Exception as e:
        return f"Error: {str(e)}"

# Test the function
if __name__ == "__main__":
    print(tentacle('[3,1,4,2]'))  # Should print: 4
    print(tentacle('[10, -5, 0, 7]'))  # Should print: 10
    print(tentacle('[3.14, 2.71, 1.41]'))  # Should print: 3.14
    print(tentacle('[a, b, c]'))  # Should print: Error: List must contain only numbers.
    print(tentacle('not a list'))  # Should print: Error: ...