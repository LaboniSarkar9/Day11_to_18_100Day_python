import art
print(art.logo)
from random import randint

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5



# function to check users guess against the answer
def check_answer(user_guess, actual_answer,turns):
    """Checks answer against guess, returns the number of turns remaining"""
    if user_guess > actual_answer:
        print("Too high.")
        return turns-1
    elif user_guess < actual_answer:
        print("Too Low")
        return turns-1
    else:
        print(f"You got it! The answer was {actual_answer}")


# Function to set difficulty
def set_difficulty():
    level=input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    # choose a number between 1 and 100.
    print("Welcome to the guessing game!")
    print("I am thinking of a number between 1  and 100.")
    answer = randint(1,100)
    print(f"Pssst, the correct answer is {answer}")

    turns = set_difficulty()

    guess = 0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        #Let the user guess a number
        guess = int(input("Make a Guess: "))

        # track the number of turns and reduce by 1.

        turns = check_answer(guess,answer,turns)
        # Function to check users' guess against actual answer
        if turns == 0:
            print("You have run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")


game()
