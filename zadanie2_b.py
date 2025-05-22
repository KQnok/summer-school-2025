print('Welcome to Spelling Bee!\n'
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

print(f'Game over! Your final score is: {final_score}')


#spellingcheck for pro