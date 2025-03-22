import re
import string

def tool(input_string, case='lower', remove_punctuation=False, trim_whitespace=True, 
         remove_extra_spaces=True, replace_newlines=' ', replace_numbers=None,
         custom_replacements=None, preserve_formatting=False, preserve_acronyms=False):
    """
    Process the input string with various text manipulation options.

    Args:
    input_string (str): The input string to be processed.
    case (str): The desired case for the output. Options are 'lower', 'upper', or 'title'. Default is 'lower'.
    remove_punctuation (bool): If True, remove all punctuation from the string. Default is False.
    trim_whitespace (bool): If True, remove leading and trailing whitespace. Default is True.
    remove_extra_spaces (bool): If True, remove extra spaces between words. Default is True.
    replace_newlines (str or None): Replace newlines with this string. If None, keep newlines. Default is ' '.
    replace_numbers (str or None): Replace numbers with this string. If None, keep numbers. Default is None.
    custom_replacements (dict or None): A dictionary of custom replacements. 
                                        Keys are regex patterns, values are replacement strings. Default is None.
    preserve_formatting (bool): If True, apply case conversion and replacements while preserving original formatting.
                                Default is False.
    preserve_acronyms (bool): If True, preserve acronyms when converting to lower case. Default is False.

    Returns:
    str: The processed string according to the specified options.
    """
    # Convert to desired case
    if case == 'lower':
        case_func = lambda s: s.lower() if not preserve_acronyms else _preserve_acronyms(s.lower())
    elif case == 'upper':
        case_func = str.upper
    elif case == 'title':
        case_func = str.title
    else:
        raise ValueError("Invalid case option. Use 'lower', 'upper', or 'title'.")

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
            result = re.sub(pattern, replacement, result)

    return result

def _preserve_acronyms(text):
    """
    Preserve acronyms in the given text by capitalizing them.
    
    Args:
    text (str): The input text to process.
    
    Returns:
    str: The processed text with acronyms capitalized.
    """
    words = text.split()
    for i, word in enumerate(words):
        if word.isupper() and len(word) > 1:
            words[i] = word.upper()
    return ' '.join(words)