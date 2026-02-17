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
a = int(input("a = "))
b = int(input("b = "))
correction = (a%b!=0)
print("result:", int(a/b)+correction)
