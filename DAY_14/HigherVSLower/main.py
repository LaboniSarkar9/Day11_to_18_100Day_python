# display art
from art import logo,vs
from game_data import data
import random

#Format the account data into printable format.
def format_data(account):
    """ Takes the account data and returns the printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """ Take a user's guess and the follower counts and returns if they got it """
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess =="b"
print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
#Make the game repeatable.
while game_should_continue:
    # Generate random account from the game data
    account_a = account_b
    account_b = random.choice(data)
    if account_a == account_b:
        account_b=random.choice(data)

    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Compare B: {format_data(account_b)}.")

    #Ask user for a guess
    guess = input("Who has more followers? Type 'A' or 'B' ").lower()

    print("\n"*20)
    print(logo)

    ## get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # Check if user is correct.
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    ## use if statement to check if user is correct.

    #Give user feedback on their guess.
    # score keeping
    if is_correct:
        score += 1
        print(f"You're right! Current score {score} ")
    else:
        print(f"Sorry, that's wrong. Final Score {score}")





#Making account at position B becom the next account at position A.

