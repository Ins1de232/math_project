import random

def greet():
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")
    return name

def generate_progression(length=10, start=0, step=1):
    return [start + i * step for i in range(length)]

def brain_progression():
    name = greet()
    print("What number is missing in the progression?")
    rounds = 3
    for _ in range(rounds):
        length = random.randint(5, 10)
        start = random.randint(1, 20)
        step = random.randint(1, 10)
        progression = generate_progression(length, start, step)
        
        hidden_index = random.randint(0, length - 1)
        correct_answer = progression[hidden_index]
        question_list = [str(num) for num in progression]
        question_list[hidden_index] = ".."
        question_str = " ".join(question_list)
        
        print(f"Question: {question_str}")
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
    brain_progression()