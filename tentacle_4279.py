# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Find the maximum value in a list of numbers.

    Args:
    numbers (list): A list of numbers.

    Returns:
    str: The maximum value in the list as a string.

    Example:
    >>> tentacle([3, 1, 4, 2])
    '4'
    """
    # Check if the input list is empty
    if not numbers:
        return "Error: Empty list"

    # Find the maximum value in the list
    max_value = max(numbers)

    # Convert the result to a string and return it
    return str(max_value)

# Test the function
if __name__ == "__main__":
    print(tentacle([3, 1, 4, 2]))  # Should print: '4'
    print(tentacle([-5, 0, 10, -1]))  # Should print: '10'
    print(tentacle([1]))  # Should print: '1'
    print(tentacle([]))  # Should print: 'Error: Empty list'