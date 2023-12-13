import random
logo=('''_________                              ___________                                    ______              
__  ____/___  _____________________    __  /___  /______     ___________  ________ ______  /______________
_  / __ _  / / /  _ \_  ___/_  ___/    _  __/_  __ \  _ \    __  __ \  / / /_  __ `__ \_  __ \  _ \_  ___/
/ /_/ / / /_/ //  __/(__  )_(__  )     / /_ _  / / /  __/    _  / / / /_/ /_  / / / / /  /_/ /  __/  /    
\____/  \__,_/ \___//____/ /____/      \__/ /_/ /_/\___/     /_/ /_/\__,_/ /_/ /_/ /_//_.___/\___//_/''')

# Including two different difficulty levels.
def user_attempts():
    attempts=0
    if difficulty_level== "easy":
        attempts+=10
        return attempts
    else:
        attempts+=5
        return attempts
# Generating a random number
def correct_answer():
    chosen_number= random.randint(1,101)
    return chosen_number
print(logo)
print("Welcome to the number guessing game!")
print("I'm thinking of a number between 1 and 100")
difficulty_level= input("Type 'easy' or 'hard': ").lower()
print(f"You have only {user_attempts()} attempts")
number_chosen=correct_answer()
number_of_attempts= user_attempts()


should_continue= True
while should_continue:
    # Allow the player to submit a guess for a number between 1 and 100.
    user_guess= int(input("Make a guess: "))
    # Check user's guess against actual answer. "Too high." or "Too low." depending on the user's answer.
    if user_guess == number_chosen:
        should_continue = False
        print(f"You got it! The answer was {number_chosen}")

    elif user_guess != number_chosen and user_guess > number_chosen:
        print("Too high.\nGuess again.")
        number_of_attempts-= 1
        print(f"You have {number_of_attempts} attempts remaining")
        # check if user runs out of attempts
        if  number_of_attempts == 0:
            should_continue= False

    elif user_guess != number_chosen and user_guess < number_chosen:
        print("Too low. \nGuess again.")
        number_of_attempts-= 1
        print(f"You have {number_of_attempts} attempts remaining")
        #check if user runs out of attempts
        if number_of_attempts == 0:
            should_continue = False
            print("Game Over!")
