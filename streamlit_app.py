import streamlit as st
import random

# Initialize session state if not already set
if 'attempts' not in st.session_state:
    st.session_state.attempts = 6
if 'guessed_letters' not in st.session_state:
    st.session_state.guessed_letters = set()
if 'game_status' not in st.session_state:
    st.session_state.game_status = "Playing"
if 'chosen_word' not in st.session_state:
    st.session_state.chosen_word = ""
if 'placeholder' not in st.session_state:
    st.session_state.placeholder = ""

# List of words for the game
word_list = ["Pythonic", "looping", "coding"]

def select_random_word(word_list):
    return random.choice(word_list)

def initialize_placeholder(word_length):
    return "_" * word_length

def update_placeholder(chosen_word, placeholder, guess):
    placeholder = list(placeholder)
    for i, letter in enumerate(chosen_word):
        if letter.lower() == guess:
            placeholder[i] = letter
    return ''.join(placeholder)

def display_placeholder(placeholder):
    return ' '.join(placeholder)

def initialize_game():
    st.session_state.chosen_word = select_random_word(word_list)
    st.session_state.word_length = len(st.session_state.chosen_word)
    st.session_state.placeholder = initialize_placeholder(st.session_state.word_length)
    st.session_state.attempts = 6
    st.session_state.guessed_letters = set()
    st.session_state.game_status = "Playing"

def word_guess_game():
    if st.session_state.game_status == "Game Over":
        st.write("Game has been reset. Please enter a new guess.")
    
    st.title("Word Guess Game")

    # Display the current state of the placeholder
    st.write(display_placeholder(st.session_state.placeholder))

    guess = st.text_input("Guess a letter:", max_chars=1).lower()

    if guess:
        if not guess.isalpha() or len(guess) != 1:
            st.write("Invalid input. Please enter a single letter.")
        elif guess in st.session_state.guessed_letters:
            st.write("You've already guessed that letter.")
        else:
            st.session_state.guessed_letters.add(guess)
            if guess in st.session_state.chosen_word.lower():
                st.session_state.placeholder = update_placeholder(st.session_state.chosen_word, st.session_state.placeholder, guess)
                st.write("Good guess!")
            else:
                st.session_state.attempts -= 1
                st.write(f"Wrong guess! You have {st.session_state.attempts} attempts left.")

        st.write(display_placeholder(st.session_state.placeholder))

        # Check game status
        if "_" not in st.session_state.placeholder:
            st.write(f"Congratulations! You've guessed the word: {st.session_state.chosen_word}")
            st.session_state.game_status = "Game Over"
        elif st.session_state.attempts <= 0:
            st.write(f"Game over! The word was: {st.session_state.chosen_word}")
            st.session_state.game_status = "Game Over"

    # Reset game state
    if st.button("Reset Game"):
        initialize_game()
        st.write("Game has been reset. Please enter a new guess.")

# Run the game
word_guess_game()
