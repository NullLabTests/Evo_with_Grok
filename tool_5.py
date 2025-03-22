import string

def tool(input_string, case='lower', remove_punctuation=False, trim_whitespace=True, replace_spaces=False):
    """
    Process the input string with various text manipulation options.

    Args:
    input_string (str): The input string to be processed.
    case (str): The desired case for the output. Options are 'lower', 'upper', or 'title'. Default is 'lower'.
    remove_punctuation (bool): If True, remove all punctuation from the string. Default is False.
    trim_whitespace (bool): If True, remove leading and trailing whitespace. Default is True.
    replace_spaces (bool): If True, replace spaces with underscores. Default is False.

    Returns:
    str: The processed string according to the specified options.
    """
    # Convert to desired case
    if case == 'lower':
        result = input_string.lower()
    elif case == 'upper':
        result = input_string.upper()
    elif case == 'title':
        result = input_string.title()
    else:
        raise ValueError("Invalid case option. Use 'lower', 'upper', or 'title'.")

    # Remove punctuation if specified
    if remove_punctuation:
        result = result.translate(str.maketrans('', '', string.punctuation))

    # Replace spaces with underscores if specified
    if replace_spaces:
        result = result.replace(' ', '_')

    # Trim whitespace if specified
    if trim_whitespace:
        result = result.strip()

    return result