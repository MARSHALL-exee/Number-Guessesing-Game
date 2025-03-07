# Number Guessing Game
import random
top_of_range = input("Type a number: ")

# Check if the input is a digit
if top_of_range.isdigit():
    top_of_range = int(top_of_range)  # Convert the input to an integer

    # Check if the number is greater than 0
    if top_of_range <= 0:
        print("Please type a number larger than 0 next time.")
        quit()  # Exit the program if the number is not greater than 0
else:
    print("Please type a number next time.")
    quit()

# Generate a random number between 0 and the user-defined upper limit
random_number = random.randrange(0, top_of_range)
guesses = 0  # Initialize the number of guesses

# Start the guessing loop
while True:
    guesses += 1  # Increment the guess count
    user_guess = input("Make a guess: ")

    # Check if the guess is a digit
    if user_guess.isdigit():
        user_guess = int(user_guess)  # Convert the guess to an integer
    else:
        print("Please type a number next time.")
        continue  # Continue to the next iteration if the guess is not a digit
    
    # Check if the guess is correct
    if user_guess == random_number:
        print("You got it!")
        break
    else:
        print("Try again!")

# Print the total number of guesses it took to guess correctly
print("It took you", guesses, "guesses!")