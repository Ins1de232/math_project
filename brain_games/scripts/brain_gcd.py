import random

def greet():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def brain_gcd():
    name = greet()
    print("Find the greatest common divisor of given numbers.")
    rounds = 3
    for _ in range(rounds):
        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        correct_answer = gcd(num1, num2)
        print(f"Question: {num1} {num2}")
        user_input = input("Your answer: ").strip()
        if not user_input.lstrip('-').isdigit():
            print(f"'{user_input}' is not a number. Let's try again, {name}!")
            return
        user_answer = int(user_input)
        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_input}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return
    print(f"Congratulations, {name}!")

if __name__ == "__main__":
    brain_gcd()