import re
import string

def tool(input_string, case='lower', remove_punctuation=False, trim_whitespace=True, 
         replace_punctuation_with='', remove_digits=False, custom_regex=None):
    """
    Process the input string with various text manipulation options.

    Args:
    input_string (str): The input string to be processed.
    case (str): The desired case for the output. Options are 'lower', 'upper', or 'title'. Default is 'lower'.
    remove_punctuation (bool): If True, remove all punctuation from the string. Default is False.
    trim_whitespace (bool): If True, remove leading and trailing whitespace. Default is True.
    replace_punctuation_with (str): If set, replace punctuation with this string. Overrides remove_punctuation.
    remove_digits (bool): If True, remove all digits from the string. Default is False.
    custom_regex (str): If set, apply this regex pattern to the string for custom processing.

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

    # Remove or replace punctuation if specified
    if replace_punctuation_with:
        result = result.translate(str.maketrans(string.punctuation, replace_punctuation_with * len(string.punctuation)))
    elif remove_punctuation:
        result = result.translate(str.maketrans('', '', string.punctuation))

    # Remove digits if specified
    if remove_digits:
        result = ''.join(char for char in result if not char.isdigit())

    # Trim whitespace if specified
    if trim_whitespace:
        result = result.strip()

    # Apply custom regex if specified
    if custom_regex:
        result = re.sub(custom_regex, '', result)

    return result