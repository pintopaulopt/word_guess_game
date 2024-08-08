import random

def select_random_word(word_list):
    """
    Select a random word from the provided list.

    Args:
        word_list (list): A list of words to choose from.

    Returns:
        str: A randomly chosen word from the list.
    """
    return random.choice(word_list)

def initialize_placeholder(word_length):
    """
    Initialize the placeholder with underscores to represent unguessed letters.

    Args:
        word_length (int): The length of the chosen word.

    Returns:
        list: A list of underscores ('_') with the same length as the chosen word.
    """
    return ["_"] * word_length

def update_placeholder(chosen_word, placeholder, guess):
    """
    Update the placeholder with the guessed letter in the correct positions.

    Args:
        chosen_word (str): The word that the player is trying to guess.
        placeholder (list): The current state of the word being guessed, represented by underscores and correctly guessed letters.
        guess (str): The letter guessed by the player.

    Returns:
        list: The updated placeholder with the guessed letter in the correct positions.
    """
    for position in range(len(chosen_word)):
        # Check if the guessed letter matches the current letter in the word, ignoring case.
        if chosen_word[position].lower() == guess:
            # Update the placeholder with the correctly guessed letter, preserving its original case.
            placeholder[position] = chosen_word[position]
    return placeholder

def display_placeholder(placeholder):
    """
    Display the current state of the placeholder, separating each character with a space.

    Args:
        placeholder (list): The current state of the word being guessed.

    Returns:
        str: The placeholder as a string with spaces between each character.
    """
    return " ".join(placeholder)

def word_guess_game():
    """
    Run the Word Guess Game, a simplified version of Hangman.

    The game allows the player to guess letters in a randomly chosen word.
    The player has a limited number of incorrect guesses (attempts) before the game ends.
    """
    word_list = ["Pythonic", "looping", "coding"]  # List of possible words to guess.
    chosen_word = select_random_word(word_list)  # Randomly select a word from the list.
    word_length = len(chosen_word)  # Determine the length of the chosen word.
    placeholder = initialize_placeholder(word_length)  # Initialize the placeholder with underscores.
    
    print("Welcome to Word Guess Game!")
    print(display_placeholder(placeholder))  # Display the initial state of the placeholder.
    
    attempts = 6  # Set the number of allowed incorrect guesses.
    guessed_letters = set()  # Initialize an empty set to store guessed letters.
    
    while "_" in placeholder and attempts > 0:
        guess = input("Guess a letter: ").lower()  # Prompt the player to guess a letter and convert it to lowercase.
        
        # Validate the input: must be a single alphabetical character.
        if not guess.isalpha() or len(guess) != 1:
            print("Invalid input. Please enter a single letter.")
            continue
        
        # Check if the letter has already been guessed.
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        guessed_letters.add(guess)  # Add the guessed letter to the set of guessed letters.
        
        # Check if the guessed letter is in the chosen word.
        if guess in chosen_word.lower():
            placeholder = update_placeholder(chosen_word, placeholder, guess)  # Update the placeholder with the guessed letter.
            print("Good guess!")
        else:
            attempts -= 1  # Decrement the number of remaining attempts for an incorrect guess.
            print(f"Wrong guess! You have {attempts} attempts left.")
        
        print(display_placeholder(placeholder))  # Display the updated placeholder.
    
    # Check if the player has successfully guessed the word.
    if "_" not in placeholder:
        print(f"Congratulations! You've guessed the word: {chosen_word}")
    else:
        print(f"Game over! The word was: {chosen_word}")

# This block ensures that the game runs only when the script is executed directly.
if __name__ == "__main__":
    word_guess_game()  # Start the Word Guess Game.
