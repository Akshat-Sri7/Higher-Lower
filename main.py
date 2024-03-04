import random
from game_data import data
from art import logo, vs


def get_random_account():
    return random.choice(data)


def format_data(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"


def actual_followers(a_followers, b_followers):
    """Checks amongst the two accounts, who has more followers."""
    if a_followers > b_followers:
        return 'a'
    else:
        return 'b'


def check_response(guess, a_followers, b_followers):
    """Compares the user input against the actual result."""
    if guess == actual_followers(a_followers, b_followers):
        return True
    else:
        return False


def game():
    print(logo)
    score = 0
    game_should_continue = True
    a_account = get_random_account()
    b_account = get_random_account()

    while game_should_continue:
        a_account = b_account
        b_account = get_random_account()

        while a_account == b_account:
            b_account = get_random_account()

        print("Compare A: " + format_data(a_account))
        print(vs)
        print("Against B: " + format_data(b_account))

        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        game_should_continue = check_response(choice, a_account["follower_count"], b_account["follower_count"])

        print(logo)
        if game_should_continue:
            score += 1
        print(f"You're Right! Current Score: {score}")

    print(logo)
    print(f"Sorry, That's wrong. Final score: {score}")


game()
