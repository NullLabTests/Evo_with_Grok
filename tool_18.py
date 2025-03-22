import string
import re

def tool(input_string, case='lower', remove_punctuation=False, trim_whitespace=True, 
         remove_extra_spaces=True, replace_newlines=' ', replace_numbers=None,
         custom_replacements=None, preserve_acronyms=False):
    """
    Process the input string with various text manipulation options.

    Args:
    input_string (str): The input string to be processed.
    case (str): The desired case for the output. Options are 'lower', 'upper', 'title', or 'capitalize'. Default is 'lower'.
    remove_punctuation (bool): If True, remove all punctuation from the string. Default is False.
    trim_whitespace (bool): If True, remove leading and trailing whitespace. Default is True.
    remove_extra_spaces (bool): If True, remove extra spaces between words. Default is True.
    replace_newlines (str or None): Replace newlines with this string. If None, keep newlines. Default is ' '.
    replace_numbers (str or None): Replace numbers with this string. If None, keep numbers. Default is None.
    custom_replacements (dict or None): A dictionary of custom replacements. 
                                        Keys are regex patterns, values are replacement strings. Default is None.
    preserve_acronyms (bool): If True and case is 'lower', preserve all-uppercase acronyms. Default is False.

    Returns:
    str: The processed string according to the specified options.
    """
    # Convert to desired case
    if case == 'lower':
        result = input_string.lower() if not preserve_acronyms else _preserve_acronyms(input_string.lower())
    elif case == 'upper':
        result = input_string.upper()
    elif case == 'title':
        result = input_string.title()
    elif case == 'capitalize':
        result = input_string.capitalize()
    else:
        raise ValueError("Invalid case option. Use 'lower', 'upper', 'title', or 'capitalize'.")

    # Replace newlines if specified
    if replace_newlines is not None:
        result = result.replace('\n', replace_newlines)

    # Replace numbers if specified
    if replace_numbers is not None:
        result = re.sub(r'\d+', replace_numbers, result)

    # Remove punctuation if specified
    if remove_punctuation:
        result = ''.join(char for char in result if char.isalnum() or char.isspace())

    # Remove extra spaces if specified
    if remove_extra_spaces:
        result = ' '.join(result.split())

    # Trim whitespace if specified
    if trim_whitespace:
        result = result.strip()

    # Apply custom replacements if specified
    if custom_replacements:
        for pattern, replacement in custom_replacements.items():
            result = re.sub(pattern, replacement, result)

    return result

def _preserve_acronyms(text):
    """
    Preserve all-uppercase acronyms in a lowercased string.

    Args:
    text (str): The input string with all characters lowercased.

    Returns:
    str: The input string with acronyms preserved as uppercase.
    """
    words = text.split()
    for i, word in enumerate(words):
        if word.isupper() and len(word) > 1:
            words[i] = word.upper()
    return ' '.join(words)