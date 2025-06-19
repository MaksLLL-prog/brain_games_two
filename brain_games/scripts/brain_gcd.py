import random
from brain_games.cli import welcome_user
from math import gcd

def generate_question():
    a = random.randint(1, 50)
    b = random.randint(1, 50)
    correct_answer = str(gcd(a, b))
    question = f"{a} {b}"
    return question, correct_answer

def play_gcd_game():
    name = welcome_user()
    print("Find the greatest common divisor of given numbers.")
    
    correct_answers = 0
    while correct_answers < 3:
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(f"'{user_answer}' is wrong ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")

def main():
    play_gcd_game()

if __name__ == "__main__":
    main()