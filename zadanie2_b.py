"""print('Welcome to Spelling Bee!\n'
      'Today\'s letters are ACILMTY and the letter of the day is T\n'
      'Feel free to press XXXXX when you\'re done playing')

req_letters = ['a', 'c', 'i', 'l', 'm', 't', 'y']
center_letter = 't'
final_score = 0

all_words = ['ALIT', 'AMITY', 'ATILT', 'ATTIC', 'CACTI', 'CALAMITY', 'CATALYTIC',
             'CATALYTICALLY', 'CATCALL', 'CATTAIL', 'CATTILY', 'CATTY', 'CITY',
             'CLIMACTIC', 'CLIMACTICALLY', 'CLIMATIC', 'CLIMATICALLY', 'ILLICIT',
             'ILLICITLY', 'ITALIC', 'ITTY', 'LACTIC', 'LAITY', 'LICIT', 'LICITLY',
             'LILT', 'LIMIT', 'MALT', 'MALTY', 'MILITIA', 'MITT', 'TACIT', 'TACITLY',
             'TACT', 'TACTIC', 'TACTICAL', 'TACTICALLY', 'TACTILITY', 'TAIL', 'TALC',
             'TALI', 'TALL', 'TALLIT', 'TALLY', 'TATAMI', 'TATTY', 'TILL', 'TILT']

used_words = []

while True:
    suggested_word = input('Please enter a word: ').upper()

    if suggested_word == 'XXXXX':
        break

    if not suggested_word.isalpha():
        print('Sorry, those clearly aren\'t letters')
        continue

    if len(suggested_word) <= 3:
        print('Sorry, the word is too short')
        continue

    if center_letter.upper() not in suggested_word:
        print('Must contain the center letter of the day - T')
        continue

    invalid_letter = False
    for letter in suggested_word:
        if letter not in [x.upper() for x in req_letters]:
            print('Todays letters are only ACILMTY.Sorry, you used letters out of that range(')
            invalid_letter = True
            break
    if invalid_letter:
        continue

    if suggested_word in used_words:
        print('Sorry, you\'ve already used this word. Try another')
        continue

    if suggested_word not in all_words:
        print('Sorry, this word seems to not exist')
        continue
    else:
        used_words.append(suggested_word)


    word_length = len(suggested_word)
    if word_length == 4:
        points = 1
    elif 5 <= word_length <= 7:
        points = word_length
    else:
        points = word_length * 2

    final_score += points
    print(f'Cool! You found the word  "{suggested_word}" you earned {points} points')

print(f'Game over! Your final score is: {final_score}'"""

import requests

def is_valid_english_word(word):
    try:
        response = requests.get(
            f"https://api.dictionaryapi.dev/api/v2/entries/en/{word.lower()}",
            timeout=3
        )
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def calculate_points(word):
    length = len(word)
    if length == 4:
        return 1
    elif 5 <= length <= 7:
        return length
    else:
        return length * 2


def is_valid_word(word, letters, center_letter):
    word = word.lower()
    letters = [l.lower() for l in letters]
    center_letter = center_letter.lower()

    if len(word) < 4:
        return False, "Word is too short (minimum 4 letters)"

    if center_letter not in word:
        return False, "Must contain the center letter"

    for letter in word:
        if letter not in letters:
            return False, f"Invalid letter '{letter}'. Allowed letters: {''.join(letters).upper()}"

    return True, ""


def play_spelling_bee(letters, center_letter):
    letters = [l.lower() for l in letters]
    center_letter = center_letter.lower()

    print(f"\nWelcome to Spelling Bee!")
    print(f"Today's letters: {''.join(letters).upper()}")
    print(f"Center letter: {center_letter.upper()}")
    print("Enter words (or 'XXXXX' to quit):\n")

    score = 0
    used_words = set()

    while True:
        word = input("Your word: ").strip().lower()

        if word == 'xxxxx':
            break

        is_valid, message = is_valid_word(word, letters, center_letter)
        if not is_valid:
            print(f"Invalid: {message}")
            continue

        # Check if word exists in dictionary
        if not is_valid_english_word(word):
            print("Word not found in dictionary")
            continue

        # Check if already used
        if word in used_words:
            print("You already used this word")
            continue

        # Calculate points
        points = calculate_points(word)
        score += points
        used_words.add(word)

        print(f"✓ Found '{word.upper()}'! +{points} points (Total: {score})")

    print(f"\nGame over! Final score: {score}")
    if used_words:
        print("Your words:", ', '.join(sorted(used_words, key=lambda x: (-len(x), x))))


import random
from string import ascii_lowercase


def generate_spelling_bee_letters():
    vowels = {'a', 'e', 'i', 'o', 'u'}
    consonants = set(ascii_lowercase) - vowels

    selected_letters = random.sample(sorted(vowels), k=1)

    remaining_letters = random.sample(sorted(consonants), k=6)
    selected_letters.extend(remaining_letters)

    random.shuffle(selected_letters)
    center_letter = random.choice(selected_letters)

    return sorted(selected_letters), center_letter


def main():

    letters, center_letter = generate_spelling_bee_letters()

    play_spelling_bee(letters, center_letter)


if __name__ == "__main__":
    main()