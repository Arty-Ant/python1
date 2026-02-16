"""
Задача № 1.
Получить реверсную запись трехзначного числа
Пример:
вход: 346, выход: 643
вход: 100, выход: 001
вход: 340, выход: 043

Индексы и слайсы еще не существуют!
Подсказка: // и %
"""

user_number = int(input("Введите трёхзначное число: "))
first_number = user_number//100
second_number = (user_number-first_number*100)//10
third_number = user_number-(first_number*100+second_number*10)
print("Палиндром вашего числа:",str(third_number*100)+str(second_number*10)+str(first_number))

