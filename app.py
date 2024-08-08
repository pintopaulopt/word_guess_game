import streamlit as st
from word_guess_game import select_random_word, initialize_placeholder, update_placeholder, display_placeholder

# List of words for the game
word_list = ["Pythonic", "looping", "coding"]

def word_guess_game():
    chosen_word = select_random_word(word_list)
    word_length = len(chosen_word)
    placeholder = initialize_placeholder(word_length)

    st.title("Word Guess Game")

    # Initialize the game state
    if 'attempts' not in st.session_state:
        st.session_state.attempts = 6
        st.session_state.guessed_letters = set()

    # Display the initial state of the placeholder
    st.write(display_placeholder(placeholder))

    guess = st.text_input("Guess a letter:", max_chars=1).lower()

    if guess:
        # Check if the letter has already been guessed
        if guess in st.session_state.guessed_letters:
            st.write("You've already guessed that letter.")
        else:
            st.session_state.guessed_letters.add(guess)
            if guess in chosen_word.lower():
                placeholder = update_placeholder(chosen_word, placeholder, guess)
                st.write("Good guess!")
            else:
                st.session_state.attempts -= 1
                st.write(f"Wrong guess! You have {st.session_state.attempts} attempts left.")

        st.write(display_placeholder(placeholder))

        # Check if the player has successfully guessed the word
        if "_" not in placeholder:
            st.write(f"Congratulations! You've guessed the word: {chosen_word}")
            st.session_state.attempts = 6
            st.session_state.guessed_letters = set()
        elif st.session_state.attempts <= 0:
            st.write(f"Game over! The word was: {chosen_word}")
            st.session_state.attempts = 6
            st.session_state.guessed_letters = set()

# Run the game
word_guess_game()
