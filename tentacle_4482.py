# Domains: text processing, mathematics
def tentacle(numbers):
    """
    Find the maximum value in a list of numbers.

    Args:
    numbers (list): A list of numbers.

    Returns:
    int or float: The maximum value in the list.

    Example:
    >>> tentacle([3, 1, 4, 2])
    4
    """
    # Check if the input list is empty
    if not numbers:
        raise ValueError("The input list is empty")

    # Initialize the maximum value with the first element
    max_value = numbers[0]

    # Iterate through the list to find the maximum value
    for num in numbers[1:]:
        if num > max_value:
            max_value = num

    return max_value

# Test the function
if __name__ == "__main__":
    print(tentacle([3, 1, 4, 2]))  # Should print: 4
    print(tentacle([-5, 0, 10, -1]))  # Should print: 10
    print(tentacle([3.14, 2.71, 1.41, 0.58]))  # Should print: 3.14