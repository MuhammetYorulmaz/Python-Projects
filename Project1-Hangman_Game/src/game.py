import json
import random
from src.utils import get_random_word, display_hangman
def start_game():
    with open('data/words.json', 'r') as file:
        words = json.load(file)
    word = get_random_word(words['words'])
    right_to_try = 6
    count_of_guessed_world = '_' * len(word)
    guessed_correctly = False
    guessed_letter = []

    print("Let's Play Hangman!")
    print(display_hangman(right_to_try))
    print(count_of_guessed_world)
    print("\n")

    while not guessed_letter and right_to_try > 0:
        pass

    if guessed_correctly:
        print(f'Congratulations! You guessed the word "{word}" correctly')
    else:
        print(f'Unfortunately, your right to try has expired. The word was: {word}')
