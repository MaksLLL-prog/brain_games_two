import random
from brain_games.cli import welcome_user

def is_even(number):
    return number % 2 == 0

def play_even_game():
    name = welcome_user()
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    
    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f"Question: {number}")
        answer = input("Your answer: ").strip().lower()
        
        correct = "yes" if is_even(number) else "no"
        if answer == correct:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct}'.")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")

def main():
    play_even_game()

if __name__ == "__main__":
    main()