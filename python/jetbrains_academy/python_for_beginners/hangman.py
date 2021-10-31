import random


def should_start_game():
    # Ask user if they want to play the game
    print("H A N G M A N")

    user_choice = None
    while user_choice not in ("play", "exit"):
        user_choice = input('Type "play" to play the game, "exit" to quit: ')
    return user_choice == "play"


def is_game_over(num_lives, word, current_word):
    # Return a boolean indicating if the game is over
    return num_lives <= 0 or word == current_word


def get_word():
    # Randomly choose a word and return it
    words = ["python", "java", "kotlin", "javascript"]
    return random.choice(words)


def get_initial_hint(word):
    # Generate the initial hint based on the word length
    return HIDDEN_CHAR * len(word)


def get_guess(current_word):
    # Get the user's guess for a letter
    print(f"\n{current_word}")
    guess = input(f"Input a letter: ")
    return guess


def check_guess(num_lives, guess, guessed_letters, word, current_word):
    # Check if the guessed letter is in the word and update the guessed word
    updated_word = current_word

    if len(guess) != 1:
        print("You should input a single letter")
    elif guess.isupper() or not guess.isalpha():
        print("Please enter a lowercase English letter")
    elif guess in word:
        if guess not in guessed_letters:
            updated_word = []
            for index, char in enumerate(current_word):
                if char == HIDDEN_CHAR and word[index] == guess:
                    updated_word.append(word[index])
                else:
                    updated_word.append(char)
            updated_word = "".join(updated_word)
        else:
            print("You've already guessed this letter")
    elif guess in guessed_letters:
        print("You've already guessed this letter")
    else:
        print("That letter doesn't appear in the word")
        num_lives -= 1

    return num_lives, updated_word


def print_result(word, current_word):
    # Print end of game message
    if word == current_word:
        print(f"\n{current_word}")
        print("You guessed the word!")
        print("You survived!")
    else:
        print("You lost!")


if __name__ == '__main__':
    HIDDEN_CHAR = "-"

    num_lives = 8
    word = get_word()
    current_word = get_initial_hint(word)
    guessed_letters = set()

    if should_start_game():
        while not is_game_over(num_lives, word, current_word):
            guess = get_guess(current_word)
            num_lives, current_word = check_guess(num_lives,
                                                  guess,
                                                  guessed_letters,
                                                  word,
                                                  current_word)
            guessed_letters.add(guess)

        print_result(word, current_word)
