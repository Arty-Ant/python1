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
# Variant 1
inside_number = int(input("Введите число: "))
first_symbol = inside_number // 100
second_symbol = inside_number % 100 // 10
third_symbol = inside_number % 10
print(third_symbol, second_symbol, first_symbol, sep="")

# Variant 2
num = int(input('Enter a number(3 digit): '))
out = str(num % 10) + str(num % 100 // 10) + str(num // 100)
print("Reverse the number: ", out)

# Variant 3
xyz = int(input("Введи трёхзначное число: "))
x = xyz // 100
y = (xyz // 10) % 10
z = xyz % 10
# str.zfill(positions qty) - zero fill
print(str(z * 100 + y * 10 + x).zfill(3))

# Variant 4
user_number = int(input("Введите трёхзначное число: "))
first_number = user_number // 100
second_number = (user_number - first_number * 100) // 10
third_number = user_number - (first_number * 100 + second_number * 10)
print("Палиндром вашего числа:", str(third_number) + str(second_number) + str(first_number))

