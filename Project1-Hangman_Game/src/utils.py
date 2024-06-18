import random


def get_random_word(words: list) -> str:
    """
    Selects and returns a random word from a given list of words.

    Parameters:
    words (list): A list of words (strings) from which to choose a random word.

    Returns:
    str: A randomly selected word from the input list.

    Raises:
    ValueError: If the input list is empty.

    Example:
    >>> _words = ['apple', 'banana', 'cherry']
    >>> get_random_word(_words)
    'banana'
    """
    if not words:
        raise ValueError("The input list must not be empty.")
    return random.choice(words)


def display_hangman(tries: int) -> str:
    """
    Returns a string representation of the hangman game state corresponding to the number of tries remaining.

    Parameters:
    tries (int): The number of tries remaining (typically between 0 and 6).

    Returns:
    str: A string representation of the current hangman state.

    Raises:
    IndexError: If `tries` is not in the valid range (0 to 6).

    Example:
    >>> print(display_hangman(3))
         ____
        |/   |
        |   (_)
        |   \|
        |    |
        |
        |
        |_____
    """
    hangman_pic = [r"""
     ____
    |/   |
    |   (_)
    |   \|/
    |    |
    |   / \
    |
    |_____
    """,
    """
     ____
    |/   |
    |   (_)
    |   \|/
    |    |
    |   / 
    |
    |_____
    """,
    """
     ____
    |/   |
    |   (_)
    |   \|/
    |    |
    |    
    |
    |_____
    """,
    """
     ____
    |/   |
    |   (_)
    |   \|
    |    |
    |    
    |
    |_____
    """,
    """
     ____
    |/   |
    |   (_)
    |    |
    |    |    
    |    
    |
    |_____
    """,
    """
     ____
    |/   |
    |   (_)
    |    
    |    
    |    
    |
    |_____
    """,
    """
     ____
    |/   |
    |   
    |    
    |    
    |    
    |
    |_____
    """]
    return hangman_pic[tries]

