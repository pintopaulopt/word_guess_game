import streamlit as st
import random

# Function to select a random word from the provided list
def select_random_word(word_list):
    return random.choice(word_list)

# Function to initialize the placeholder with underscores
def initialize_placeholder(word_length):
    return ["_"] * word_length

# Function to update the placeholder with the guessed letter
def update_placeholder(chosen_word, placeholder, guess):
    for position in range(len(chosen_word)):
        if chosen_word[position].lower() == guess:
            placeholder[position] = chosen_word[position]
    return placeholder

# Function to display the placeholder with spaces between characters
def display_placeholder(placeholder):
    return " ".join(placeholder)

# List of possible words for the game
word_list = ["Pythonic", "looping", "coding"]

# Streamlit app layout
st.title("Word Guess Game")

# Initialize game state
if 'chosen_word' not in st.session_state:
    st.session_state.chosen_word = select_random_word(word_list)
    st.session_state.word_length = len(st.session_state.chosen_word)
    st.session_state.placeholder = initialize_placeholder(st.session_state.word_length)
    st.session_state.attempts = 6
    st.session_state.guessed_letters = set()
    st.session_state.game_status = "Playing"

# Display the current state of the placeholder
st.write(display_placeholder(st.session_state.placeholder))

# User input for guessing a letter
guess = st.text_input("Guess a letter:", max_chars=1).lower()

# Process the guess
if guess:
    if not guess.isalpha() or len(guess) != 1:
        st.error("Invalid input. Please enter a single letter.")
    elif guess in st.session_state.guessed_letters:
        st.warning("You've already guessed that letter.")
    else:
        st.session_state.guessed_letters.add(guess)
        if guess in st.session_state.chosen_word.lower():
            st.session_state.placeholder = update_placeholder(st.session_state.chosen_word, st.session_state.placeholder, guess)
            st.success("Good guess!")
        else:
            st.session_state.attempts -= 1
            st.error(f"Wrong guess! You have {st.session_state.attempts} attempts left.")

    # Check game status
    if "_" not in st.session_state.placeholder:
        st.success(f"Congratulations! You've guessed the word: {st.session_state.chosen_word}")
        st.session_state.game_status = "Game Over"
    elif st.session_state.attempts <= 0:
        st.error(f"Game over! The word was: {st.session_state.chosen_word}")
        st.session_state.game_status = "Game Over"

# Restart the game
if st.button("Restart Game"):
    st.session_state.chosen_word = select_random_word(word_list)
    st.session_state.word_length = len(st.session_state.chosen_word)
    st.session_state.placeholder = initialize_placeholder(st.session_state.word_length)
    st.session_state.attempts = 6
    st.session_state.guessed_letters = set()
    st.session_state.game_status = "Playing"
    st.experimental_rerun()
