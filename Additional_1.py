"""Напишите программу, которая
принимает на вход вещественное число
и показывает сумму его цифр.

Пример:
- 6782 -> 23
- 0,56 -> 11"""

result = 0
num = input("Введите число: ")
for i in range(0, len(num)):
    if num[i] == ",":
        continue
    elif num[i] == ".":
        continue
    result += int(num[i])
    i += 1
print(f"{num} -> {result}")