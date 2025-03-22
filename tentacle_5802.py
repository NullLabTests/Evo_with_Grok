# Domains: text processing, mathematics
def tentacle(input_list):
    """
    Find the maximum value in a list of numbers.

    Args:
    input_list (list): A list of numbers.

    Returns:
    str: The maximum value in the list as a string.

    Example:
    >>> tentacle([3, 1, 4, 2])
    '4'
    """
    # Convert the input to a list of numbers if it's a string
    if isinstance(input_list, str):
        try:
            input_list = [float(x) for x in input_list.strip('[]').split(',')]
        except ValueError:
            return "Error: Invalid input format"

    # Check if the list is empty
    if not input_list:
        return "Error: Empty list"

    # Find the maximum value in the list
    max_value = max(input_list)

    # Convert the result to a string and return it
    return str(max_value)

# Test the function
if __name__ == "__main__":
    print(tentacle([3, 1, 4, 2]))  # Should print: '4'
    print(tentacle("[-1, 0, 10, -5]"))  # Should print: '10'
    print(tentacle([]))  # Should print: 'Error: Empty list'
    print(tentacle("[a, b, c]"))  # Should print: 'Error: Invalid input format'