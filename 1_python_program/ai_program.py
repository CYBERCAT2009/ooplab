# Програма, яку запропонував AI/Copilot як "першу програму".
# Гра "Вгадай число": комп'ютер загадує число від 1 до 100,
# користувач вгадує, програма підказує "більше" / "менше".
import random

secret = random.randint(1, 100)
attempts = 0

print("Я загадав число від 1 до 100. Спробуй вгадати!")

while True:
    guess = input("Твоє число: ")
    if not guess.isdigit():
        print("Введи ціле число.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < secret:
        print("Більше!")
    elif guess > secret:
        print("Менше!")
    else:
        print(f"Вгадав! Це число {secret}. Кількість спроб: {attempts}")
        break
