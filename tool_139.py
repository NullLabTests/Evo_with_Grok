import re
from typing import Dict, Optional, Union
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

def tool(
    input_string: str,
    case: str = 'lower',
    remove_punctuation: bool = False,
    trim_whitespace: bool = True,
    remove_extra_spaces: bool = True,
    replace_newlines: Optional[str] = ' ',
    replace_numbers: Optional[str] = None,
    custom_replacements: Optional[Dict[str, Union[str, callable]]] = None,
    preserve_formatting: bool = False,
    remove_characters: Optional[str] = None,
    preserve_acronyms: bool = False,
    remove_stopwords: bool = False,
    lemmatize: bool = False,
    remove_emojis: bool = False,
    replace_urls: Optional[str] = None
) -> str:
    """
    Process the input string with various text manipulation options.

    Args:
        input_string (str): The input string to be processed.
        case (str): The desired case for the output. Options are 'lower', 'upper', or 'title'. Default is 'lower'.
        remove_punctuation (bool): If True, remove all punctuation from the string. Default is False.
        trim_whitespace (bool): If True, remove leading and trailing whitespace. Default is True.
        remove_extra_spaces (bool): If True, remove extra spaces between words. Default is True.
        replace_newlines (Optional[str]): Replace newlines with this string. If None, keep newlines. Default is ' '.
        replace_numbers (Optional[str]): Replace numbers with this string. If None, keep numbers. Default is None.
        custom_replacements (Optional[Dict[str, Union[str, callable]]]): A dictionary of custom replacements. 
            Keys are regex patterns, values are replacement strings or callables. Default is None.
        preserve_formatting (bool): If True, apply case conversion and replacements while preserving original formatting.
            Default is False.
        remove_characters (Optional[str]): A string of characters to remove from the input. Default is None.
        preserve_acronyms (bool): If True, preserve acronyms when converting to title case. Default is False.
        remove_stopwords (bool): If True, remove common stopwords from the text. Default is False.
        lemmatize (bool): If True, reduce words to their base or dictionary form. Default is False.
        remove_emojis (bool): If True, remove emojis from the text. Default is False.
        replace_urls (Optional[str]): Replace URLs with this string. If None, keep URLs. Default is None.

    Returns:
        str: The processed string according to the specified options.
    """
    # Define case conversion function
    case_func = {
        'lower': str.lower,
        'upper': str.upper,
        'title': str.title
    }.get(case)

    if case_func is None:
        raise ValueError("Invalid case option. Use 'lower', 'upper', or 'title'.")

    result = input_string

    if preserve_formatting:
        # Apply case conversion and replacements while preserving original formatting
        result = ''.join(
            case_func(char) if char.isalpha() else 
            (replace_numbers if replace_numbers and char.isdigit() else char)
            for char in result
        )
    else:
        # Apply case conversion to the entire string
        result = case_func(result)

        # Preserve acronyms when converting to title case
        if case == 'title' and preserve_acronyms:
            result = re.sub(r'\b([A-Z]{2,})\b', lambda m: m.group(1), result)

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
            if callable(replacement):
                result = re.sub(pattern, replacement, result)
            else:
                result = re.sub(pattern, replacement, result)

    # Remove specified characters if provided
    if remove_characters:
        result = ''.join(char for char in result if char not in remove_characters)

    # Remove stopwords if specified
    if remove_stopwords:
        stop_words = set(stopwords.words('english'))
        result = ' '.join(word for word in result.split() if word.lower() not in stop_words)

    # Lemmatize words if specified
    if lemmatize:
        lemmatizer = WordNetLemmatizer()
        result = ' '.join(lemmatizer.lemmatize(word) for word in result.split())

    # Remove emojis if specified
    if remove_emojis:
        emoji_pattern = re.compile("["
            u"\U0001F600-\U0001F64F"  # emoticons
            u"\U0001F300-\U0001F5FF"  # symbols & pictographs
            u"\U0001F680-\U0001F6FF"  # transport & map symbols
            u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
            u"\U00002500-\U00002BEF"  # chinese char
            u"\U00002702-\U000027B0"
            u"\U00002702-\U000027B0"
            u"\U000024C2-\U0001F251"
            u"\U0001f926-\U0001f937"
            u"\U00010000-\U0010ffff"
            u"\u2640-\u2642"
            u"\u2600-\u2B55"
            u"\u200d"
            u"\u23cf"
            u"\u23e9"
            u"\u231a"
            u"\ufe0f"  # dingbats
            u"\u3030"
            "]+", flags=re.UNICODE)
        result = emoji_pattern.sub(r'', result)

    # Replace URLs if specified
    if replace_urls is not None:
        url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        result = re.sub(url_pattern, replace_urls, result)

    return result