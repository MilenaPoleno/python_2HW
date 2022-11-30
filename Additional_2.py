"""Напишите программу, которая
принимает на вход число N и выдает
набор произведений чисел от 1 до N.

Пример:
- пусть N = 4, тогда [ 1, 2, 6, 24 ]
(1, 1*2, 1*2*3, 1*2*3*4)"""

result = []
multipler = 1
num = 1
exponent = int(input("Введите число: "))
while multipler in range(exponent + 1):
    num *= multipler
    result.append(num)
    multipler += 1
print(result)