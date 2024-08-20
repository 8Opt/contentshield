import re
import emoji    


def clean_emoji(text: str) -> str: 
    """
        Turn emoji into its word-like description. 👍 => :thumbs_up:
    """
    result = emoji.demojize(text)
    return result

def clean_extra_whitespace(text: str) -> str:
    """
        Cleans extra whitespace characters that appear between words.
    """
    cleaned_text = re.sub(r"[\xa0\n]", " ", text)
    cleaned_text = re.sub(r"([ ]{2,})", " ", cleaned_text)
    return cleaned_text.strip()

def clean_dashes(text: str) -> str:
    """
        Cleans dash characters in text.
    """

    return re.sub(r"[-\u2013]", " ", text).strip()
 
def clean(
    text: str,
    extra_whitespace: bool = False,
    dashes: bool = False,
    emoji: bool = False,
    lowercase: bool = False,
) -> str:
    """
        Cleans text.
    """

    cleaned_text = text.lower() if lowercase else text
    cleaned_text = clean_dashes(cleaned_text) if dashes else cleaned_text
    cleaned_text = clean_extra_whitespace(cleaned_text) if extra_whitespace else cleaned_text
    cleaned_text = clean_emoji(cleaned_text) if emoji else cleaned_text

    return cleaned_text.strip()

