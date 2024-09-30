import random

# Predefined list of words
words = ['python', 'javascript', 'java', 'hangman', 'programming', 'developer', 'code']

# Function to select a random word
def get_random_word():
    return random.choice(words)

# Function to display the current state of the word being guessed
def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

# Main hangman game logic
def hangman():
    word_to_guess = get_random_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(word_to_guess)} letters.")
    
    # Main game loop
    while incorrect_guesses < max_incorrect_guesses:
        print(f"\nCurrent word: {display_word(word_to_guess, guessed_letters)}")
        print(f"Incorrect guesses left: {max_incorrect_guesses - incorrect_guesses}")
        
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print(f"Good guess! {guess} is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Sorry, {guess} is not in the word.")

        if all([letter in guessed_letters for letter in word_to_guess]):
            print(f"\nCongratulations! You guessed the word: {word_to_guess}")
            break
    else:
        print(f"\nYou've run out of guesses! The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
