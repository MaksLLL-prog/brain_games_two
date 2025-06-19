import random
from brain_games.cli import welcome_user

def generate_progression(start, step, length=10):
    return [start + i * step for i in range(length)]

def generate_question():
    start = random.randint(1, 20)
    step = random.randint(1, 5)
    progression = generate_progression(start, step)
    hidden_index = random.randint(0, 9)
    correct_answer = str(progression[hidden_index])
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    return question, correct_answer

def play_progression_game():
    name = welcome_user()
    print("What number is missing in the progression?")
    
    for _ in range(3):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip()
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")

def main():
    play_progression_game()

if __name__ == "__main__":
    main()