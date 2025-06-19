import random
from brain_games.cli import welcome_user

def generate_question():
    a = random.randint(1, 20)
    b = random.randint(1, 20)
    op = random.choice(['+', '-', '*'])
    question = f"{a} {op} {b}"
    answer = str(eval(question))  # Безопасно, так как числа контролируются
    return question, answer

def play_calc_game():
    name = welcome_user()
    print("What is the result of the expression?")
    
    for _ in range(3):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong ;(. Correct was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")

def main():
    play_calc_game()

if __name__ == "__main__":
    main()