"""3) Пользователь вводит месяц в виде
целого числа от 1 до 12. Сообщить к
какому времени года относится месяц
(зима, весна, лето, осень). Напишите
решения через list и через dict."""

#list
winter = {12, 1, 2}
spring = {3, 4, 5}
summer = {6, 7, 8}
autumn = {9, 10, 11}
month = int(input("Введите месяц "
                  "(целое число от 1 до 12): "))
if month in winter:
    print("Зима")
elif month in spring:
    print("Весна")
elif month in summer:
    print("Лето")
elif month in autumn:
    print("Осень")
else: print("Введите корректное "
            "значение")

#dict
months = {"Зима": [12, 1, 2],
          "Весна": [3, 4, 5],
          "Лето": [6, 7, 8],
          "Осень": [9, 10, 11]}

month = int(input("Введите месяц "
                  "(целое число от 1 до 12): "))

for time, num in months.items():
    if month in num:
        print(time)