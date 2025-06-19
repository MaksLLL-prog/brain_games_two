from brain_games.constants import WELCOME

def welcome_user():
    print(WELCOME)
    name = input("May I have your name? ").strip()
    print(f"Hello, {name}!")
    return name
