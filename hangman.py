import functions as fc
import random
fc.clear_screen()
no_of_tries = 6
guess = False
letters_guessed = []
letters_failed = []
played_letters = []
tries = 0

words_file = open('words.txt', 'r')
words = [line.strip() for line in words_file]

word = list(random.choice(words).lower())

while tries < no_of_tries and not guess:
    letter = fc.ask_letter_user(played_letters)
    if letter in word:
        letters_guessed.append(letter)
    else:
        letters_failed.append(letter)
        tries += 1
    played_letters.append(letter)
    missing, word_so_far = fc.word_so_far(word, letters_guessed)
    # fc.display_board(letters_guessed, letters_failed, word, tries)
    fc.clear_screen()
    print(word_so_far)
    fc.draw_hangman(tries)
    if missing:
        guess = False

if guess:
    print("YOU WINN!!!!")
else:
    print("YOU LOOSEEEE")