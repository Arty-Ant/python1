"""
Задача № 2.
Введены два натуральных числа.
Округлить в большую сторону результат деления,
если числа не делятся нацело.
Про if, math, round ничего не знаем
Что знаем: +, -, *, /, //, %, **, int(), str(), bool(), float()

Пример 1:
In:
    a = 7
    b = 4
Out:
    result: 2

Пример 2:
In:
    a = 16
    b = 4
Out:
    result: 4
"""
a = int(input("a: "))
b = int(input("b: "))

# Variant 1
# Округление вверх: (a + b - 1) // b
result = (a + b - 1) // b

print("result:", result)

# Variant 2
result = (a // b) + bool(a % b)
print("result:", result)

# Variant 3
num1 = int(input('Enter a A: '))
num2 = int(input('Enter a B: '))
print("result: ", num1 // num2 + 1 - (0 ** (num1 % num2)))

# Variant 4
a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
result = (a - 1) // b + 1
print(result)

# Variant 5
a = int(input('Введите первое число'))
b = int(input('Введите второе число'))
result = (-1) * a // b  * (-1)
print(result)