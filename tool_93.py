import re
import string
from typing import Dict, Optional, Union

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
    remove_stopwords: bool = False,
    lemmatize: bool = False
) -> str:
    """
    Process the input string with various text manipulation options, including advanced NLP features.

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
        remove_stopwords (bool): If True, remove common stopwords from the text. Default is False.
        lemmatize (bool): If True, convert words to their base or dictionary form. Default is False.

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

    if preserve_formatting:
        # Apply case conversion and replacements while preserving original formatting
        result = ''.join(
            case_func(char) if char.isalpha() else 
            (replace_numbers if replace_numbers and char.isdigit() else char)
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

    # Remove punctuation if specified (using efficient method from Tool 2)
    if remove_punctuation:
        result = result.translate(str.maketrans('', '', string.punctuation))

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
        from nltk.corpus import stopwords
        import nltk
        nltk.download('stopwords', quiet=True)
        stop_words = set(stopwords.words('english'))
        result = ' '.join(word for word in result.split() if word.lower() not in stop_words)

    # Lemmatize if specified
    if lemmatize:
        from nltk.stem import WordNetLemmatizer
        import nltk
        nltk.download('wordnet', quiet=True)
        lemmatizer = WordNetLemmatizer()
        result = ' '.join(lemmatizer.lemmatize(word) for word in result.split())

    return result