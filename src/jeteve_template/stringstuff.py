"""General string functions"""


def trim(s: str) -> str:
    """
    Trim leading and trailing whitespace from a string.

    Args:
        str (str): The string to trim.

    Returns:
        str: The trimmed string.
    """
    return s.strip() if s else ""
