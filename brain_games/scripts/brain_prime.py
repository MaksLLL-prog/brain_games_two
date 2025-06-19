import random
from brain_games.cli import welcome_user

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_question():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return str(number), correct_answer

def play_prime_game():
    name = welcome_user()
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    
    for _ in range(3):
        question, correct_answer = generate_question()
        print(f"Question: {question}")
        user_answer = input("Your answer: ").strip().lower()
        
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong ;(. Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return
    
    print(f"Congratulations, {name}!")

def main():
    play_prime_game()

if __name__ == "__main__":
    main()