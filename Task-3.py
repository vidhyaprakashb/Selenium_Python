
import random  # Importing the random module to generate random numbers


# Create a method
def guess_the_number():
    computer_input = random.randint(1,10)
    # Display a welcome message
    print("Welcome to the Guess the Number Game")

    while True:
        user_input = input("Enter your number: ") # Take input from the user

        if not user_input.isdigit(): # Check if user input a valid number
            print("Please enter a number") # If user input invalid number, print this message
            continue  # Skip the rest of the loop and ask for user to input again

        user_input = int(user_input) # Convert input to an integer

        # condition to check for user input is too low, too high or correct
        if user_input < computer_input:
            print("The number you guessed is too low! Try again")
        elif user_input > computer_input:
            print("The number you guessed is too high! Try again")
        else:
            print(f"Congratulations! You guessed the correct number: {computer_input}")
            break # Correctly guessed, then exit the loop

# Call the function
guess_the_number()



def word_scramble_game():
    words = ['python', 'java', 'javascript', 'selenium', 'pytest']  # Store List of words in the list

    # Randomly select a word from the list
    computer_chosen_word = random.choice(words)

    # Scramble the selected word by shuffling its letters
    scrambled_word = ''.join(random.sample(computer_chosen_word, len(computer_chosen_word)))

    # Display a welcome message
    print("Welcome to the Word Scramble Game")
    print(f" scrambled word is : {scrambled_word}") # Show the scrambled word to the player

    # create Loop until the player correctly unscrambles the word
    while True:
        guess = input("Enter Your guess: ").lower()

        # Check if the guessed word matches the original word
        if guess == computer_chosen_word:
            print(f"Correct! the word was : {computer_chosen_word}") # Success message
            break # Exit the loop when the correct word is guessed
        else:
            print("Incorrect word! try again") # Ask the player to try again

# Start the game by calling the function
word_scramble_game()