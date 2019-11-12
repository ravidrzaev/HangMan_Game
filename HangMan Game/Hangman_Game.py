"""Hangman Game: The user enters the file path and index number of the word from the secret_words file.
The user has 6 chances to guess all the letters in the secret word. """

HANGMAN_PHOTOS = {0: """x-------x""",
                  1: """
x-------x
|
|
|
|
|""",
                  2: """
x-------x
|       |
|       0
|
|
|""",
                  3: """
x-------x
|       |
|       0
|       |
|
|""",
                  4: """
x-------x
|       |
|       0
|      /|\\
|
|""",
                  5: """
x-------x
|       |
|       0
|      /|\\
|      /
|""",
                  6: """
x-------x
|       |
|       0
|      /|\\
|      / \\
|"""}


def print_welcome_screen():
    print("WELCOME TO HANGMAN GAME!")
    print("""
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \\ / _' | '_ ' _ \\ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                       |___/
    """)


def get_file_path_from_the_user():
    """asking from the user:  file path and index number"""

    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    return choose_word(file_path, index)


def check_valid_input(letter_guessed, old_letter_guessed):
    """check if the  input from the player is valid
    return False: if the len of the input longer from 1 or is not character or the letter is guessed in the past
    else: return True"""

    if len(letter_guessed) > 1:
        return False
    if not letter_guessed.isalpha():
        return False
    if letter_guessed in old_letter_guessed:
        return False
    return True


def try_update_letter_guessed(letter_guessed, old_letter_guessed):
    """call to 'check_valid_input' function:
    if the input is valid: add the letter to list of old_letter_guessed and return true
    if the input is not valid: print 'X' and all the letter that guessed in the past, return False"""

    if check_valid_input(letter_guessed, old_letter_guessed):
        old_letter_guessed.append(letter_guessed)
        return True
    else:
        print('X')
        if len(old_letter_guessed):
            output = " -> "
            output = output.join(sorted(old_letter_guessed))
            print(output)
        return False


def show_hidden_word(secret_word, old_letter_guessed):
    """show the letter that guessed in the secret word, and print '_' for the letters that not guessed yet"""
    current_guessed_situation = ""
    for i in range(len(secret_word)):
        current_guessed_situation += "_ "
    for letter in old_letter_guessed:
        for i in range(len(secret_word)):
            if letter == secret_word[i]:
                current_guessed_situation = list(current_guessed_situation)
                current_guessed_situation[i * 2] = letter
                current_guessed_situation = "".join(current_guessed_situation)
    return current_guessed_situation


def check_win(secrete_word, old_letter_guessed):
    """check if the user win the game and guessed all the letters in the secret word.
    if all the letters in the secret word appear in the guessed list return TRUE
    else return FALSE"""

    for letter in secrete_word:
        if letter not in old_letter_guessed:
            return False
    return True


def choose_word(file_path, index):
    """open the file for read and enter all the word to list,
    return the number of words and the word that appear in the index that user choose"""

    with open(file_path, "r") as file:
        word_list = file.read()
        word_list = word_list.split(' ')
        for word in word_list:
            while word_list.count(word) > 1:
                word_list.remove(word)
        num_of_words = len(word_list)
        choose = word_list[(index - 1) % num_of_words]
        return num_of_words, choose


def print_hungman(tries):
    """print the current situation from all the photos"""
    print(HANGMAN_PHOTOS[tries])


def main():
    """main: call to all functions in order with loop until the player wins or loses"""
    old_letter_guessed = []
    print_welcome_screen()
    number_of_tries = 6
    print("You have {} tries\n".format(number_of_tries))
    num_of_words, secret_word = get_file_path_from_the_user()
    tries = 0
    print("Lets start!\n")
    print_hungman(tries)
    print(show_hidden_word(secret_word, old_letter_guessed))
    while tries < number_of_tries:
        guess_letter = input('Please guess a letter: ')
        if try_update_letter_guessed(guess_letter, old_letter_guessed):
            if guess_letter in secret_word:
                print(show_hidden_word(secret_word, old_letter_guessed))
                if check_win(secret_word, old_letter_guessed):
                    print('W I N !')
                    break
            else:
                tries += 1
                print(':(')
                print_hungman(tries)
                print('')
                print(show_hidden_word(secret_word, old_letter_guessed))

    if tries == number_of_tries:
        print('YOU LOSE!')


if __name__ == "__main__":
    main()
