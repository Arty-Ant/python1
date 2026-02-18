"""
Задача №5.
Написать программу, используя набор букв из модуля string(string.ascii_lowercase).

Вход: размер шахматной доски(NxN), где N от 0 до 20
Выход: вывести на экран эту доску с названиями полей.
Подсказка: Используем вложенные циклы

Пример:
In: 4
Out:
    a4 b4 c4 d4
    a3 b3 c3 d3
    a2 b2 c2 d2
    a1 b1 c1 d1
"""
import string as st

size=int(input("Введите размер шахматной доски от 0 до 20: "))
j=0
while j < size:
    i=0
    while i < size:
        print(st.ascii_lowercase[i]+str(size-j), end=" ")
        i+=1
    j+=1
    print()