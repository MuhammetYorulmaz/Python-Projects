import json
# import random
from src.utils import get_random_word, display_hangman


def start_game() -> None:
    with open('data/words.json', 'r') as file:
        words = json.load(file)
    word = get_random_word(words['words'])
    # print('::', word)
    right_to_try = 6
    guessed_world = '_' * len(word)
    guessed_correctly = False
    guessed_letter_list = []

    print("Let's Play Hangman!")
    # print(display_hangman(right_to_try))
    print("Guessed word: ", guessed_world)

    while not guessed_correctly and right_to_try >= 0:
        input_letter = input('Please enter a letter: ').lower()
        if input_letter.isalpha() and len(input_letter) == 1:
            if input_letter in guessed_letter_list:
                print(f'⚠️ You have already tried "{input_letter}".')
                print(f'List of entry letter that you have guessed so far: {guessed_letter_list}')
                print(display_hangman(right_to_try))
                right_to_try -= 1
            elif input_letter not in word:
                print(f'"{input_letter}" is not in the word! 😨')
                print(f'Guessed word: {guessed_world}')
                print(display_hangman(right_to_try))
                guessed_letter_list.append(input_letter)
                right_to_try -= 1
            else:
                print(f'👍 Nice! The letter "{input_letter}" is in the word.')
                guessed_letter_list.append(input_letter)
                indices_of_letter = [i for i, v in enumerate(word) if v == input_letter]
                guessed_world_list = list(guessed_world)
                for i in indices_of_letter:
                    guessed_world_list[i] = input_letter
                guessed_world = ''.join(guessed_world_list)
                print('Guessed word: ', guessed_world)

                if '_' not in guessed_world:
                    guessed_correctly = True
        else:
            print('Unexpected entry. Please enter a letter.')

    if guessed_correctly:
        print(f'🥂 Congratulations! You guessed the word "{word}" correctly')
    else:
        print(f'❌ Unfortunately, your right to try has expired. The word was: {word}')
