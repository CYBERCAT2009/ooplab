# Гра - вгадай число
# Комп'ютер загадує число, а ми маємо його вгади поступово збільшуючи або зменшуючи

import random

guest_number = random.randint(1, 100)
n_turn = 0

print("Вгадайте число від 1 до 100. Введіть 0 для виходу з гри.")
print("Введіть імя гравця: ")
name = input("Гравець: ")
print(f"Гра починається: {name}")

while True:
    n_turn += 1
    player_number = int(input("Введіть число: "))
    print(f"{name} ввів: {player_number}")
    if player_number == 0:
        print("(Легітимний вихід) Ви вийшли з гри.")
        break
    
    if player_number < 1 or player_number > 100:
        print("Введене число не в діапазоні від 1 до 100. Спробуйте ще раз.")
        continue

    if player_number < guest_number:
        print("Загадане число більше.")
    elif player_number > guest_number:
        print("Загадане число менше.")
    else:
        print(f"{name}, вітаємо! Ви вгадали число.")
        break
    

print(f"Кількість спроб: {n_turn}")
