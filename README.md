# math_project
games
# Brain Games

[![Quality gate](https://sonarcloud.io/api/project_badges/quality_gate?project=Ins1de232_math_project)](https://sonarcloud.io/summary/new_code?id=Ins1de232_math_project)


## Установка

Соберите и установите пакет:

```bash
make build
pip install --force-reinstall dist/brain_games-0.1.0-py3-none-any.whl
### четное или нет
brain-even
python brain_games/scripts/brain_even.py

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if the number is even, otherwise answer "no".
Question: 15
Your answer: no
Correct!
Question: 6
Your answer: yes
Correct!
Question: 7
Your answer: no
Correct!
Congratulations, Sam!

'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, Bill!

----

### калькулятор
python brain_games/scripts/brain_calc.py
brain-calc
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What is the result of the expression?
Question: 4 + 10
Your answer: 14
Correct!
What is the result of the expression?
Question: 25 - 11
Your answer: 14
Correct!
What is the result of the expression?
Question: 25 * 7
Your answer: 175
Correct!
Congratulations, Sam!

---

brain-calc
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What is the result of the expression?
Question: 25 * 7
Your answer: 145
'145' is wrong answer ;(. Correct answer was '175'.
Let's try again, Sam!


### Игра «НОД» (наибольший общий делитель)

Запуск:

```bash
brain-gcd
python brain_games/scripts/brain_gcd.py


Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Find the greatest common divisor of given numbers.
Question: 25 50
Your answer: 25
Correct!
Question: 100 52
Your answer: 4
Correct!
Question: 3 9
Your answer: 3
Correct!
Congratulations, Sam!
Если ответ неверный:

Question: 25 50
Your answer: 1
'1' is wrong answer ;(. Correct answer was '25'.
Let's try again, Sam!

---


### Игра «Арифметическая прогрессия»

Запуск:
python brain_games/scripts/brain_progression.py

```bash
brain-progression

Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
What number is missing in the progression?
Question: 5 7 9 11 .. 17 19 21 23
Your answer: 15
Correct!
Question: 2 5 8 .. 14 17 20 23 26 29
Your answer: 11
Correct!
Question: 14 19 24 29 34 39 44 49 54 ..
Your answer: 59
Correct!
Congratulations, Sam!
Если ответ неверный:

Question: 5 7 9 11 .. 17 19 21 23
Your answer: 1
'1' is wrong answer ;(. Correct answer was '15'.
Let's try again, Sam!

### brain_prime.py
python brain_games/scripts/brain_prime.py

Welcome to the Brain Games!
May I have your name? sam
Hello, sam!
Answer "yes" if given number is prime. Otherwise answer "no".
Question: 52
Your answer: no
Correct!
Question: 45
Your answer: NO
Correct!
Question: 71
Your answer: yes
Correct!
Congratulations, sam!