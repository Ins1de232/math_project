import random
from brain_games.cli import welcome_user


def is_even(number: int) -> bool:
    return number % 2 == 0


def main():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')

    podryad = 0

    while podryad < 3:
        question = random.randint(1, 100)
        print(f'Question: {question}')
        answer = input('Your answer: ').strip().lower()

        correct_answer = 'yes' if is_even(question) else 'no'

        if answer == correct_answer:
            print('Correct!')
            podryad += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')