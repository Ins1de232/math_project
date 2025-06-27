import random

def privet():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def operatsiya_question():
    operations = ['+', '-', '*']
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    peremen = random.choice(operations)
    question = f"{num1} {peremen} {num2}"
    if peremen == '+':
        answer = num1 + num2
    elif peremen == '-':
        answer = num1 - num2
    else:
        answer = num1 * num2
    return question, answer

def brain_calc():
    name = privet()
    rounds = 3
    for _ in range(rounds):
        question, correct_answer = operatsiya_question()
        print(f"What is the result of the expression?")
        print(f"Question: {question}")
        user_input = input("Your answer: ")
        if not user_input.strip().lstrip('-').isdigit():
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
    brain_calc()