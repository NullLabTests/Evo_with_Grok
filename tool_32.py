import re
import string

def tool(input_string, case='lower', remove_punctuation=False, trim_whitespace=True, 
         remove_extra_spaces=True, replace_newlines=' ', replace_numbers=None,
         custom_replacements=None, preserve_formatting=False, 
         preserve_case_for_replacements=False):
    """
    Process the input string with various text manipulation options.

    Args:
    input_string (str): The input string to be processed.
    case (str): The desired case for the output. Options are 'lower', 'upper', 'title', or 'preserve'. Default is 'lower'.
    remove_punctuation (bool): If True, remove all punctuation from the string. Default is False.
    trim_whitespace (bool): If True, remove leading and trailing whitespace. Default is True.
    remove_extra_spaces (bool): If True, remove extra spaces between words. Default is True.
    replace_newlines (str or None): Replace newlines with this string. If None, keep newlines. Default is ' '.
    replace_numbers (str or None): Replace numbers with this string. If None, keep numbers. Default is None.
    custom_replacements (dict or None): A dictionary of custom replacements. 
                                        Keys are regex patterns, values are replacement strings. Default is None.
    preserve_formatting (bool): If True, apply case conversion and replacements while preserving original formatting.
                                Default is False.
    preserve_case_for_replacements (bool): If True, preserve the original case when applying custom replacements.
                                           Only applies when preserve_formatting is True. Default is False.

    Returns:
    str: The processed string according to the specified options.
    """
    # Convert to desired case
    if case == 'lower':
        case_func = str.lower
    elif case == 'upper':
        case_func = str.upper
    elif case == 'title':
        case_func = str.title
    elif case == 'preserve':
        case_func = lambda x: x
    else:
        raise ValueError("Invalid case option. Use 'lower', 'upper', 'title', or 'preserve'.")

    if preserve_formatting:
        # Apply case conversion and replacements while preserving original formatting
        result = ''.join(
            case_func(char) if char.isalpha() else 
            (str.replace(char, replace_numbers) if replace_numbers and char.isdigit() else char)
            for char in input_string
        )
    else:
        # Apply case conversion to the entire string
        result = case_func(input_string)

    # Replace newlines if specified
    if replace_newlines is not None:
        result = result.replace('\n', replace_newlines)

    # Replace numbers if specified (only if preserve_formatting is False)
    if replace_numbers is not None and not preserve_formatting:
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
            if preserve_formatting and preserve_case_for_replacements:
                # Preserve case when applying custom replacements
                result = re.sub(pattern, lambda m: _preserve_case(m.group(0), replacement), result)
            else:
                result = re.sub(pattern, replacement, result)

    return result

def _preserve_case(original, replacement):
    """
    Preserve the case of the original string when applying a replacement.

    Args:
    original (str): The original string.
    replacement (str): The replacement string.

    Returns:
    str: The replacement string with the case adjusted to match the original string.
    """
    if original.isupper():
        return replacement.upper()
    elif original.islower():
        return replacement.lower()
    elif original.istitle():
        return replacement.title()
    else:
        return replacement