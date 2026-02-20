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
# Variant 1
import string as st

size = input("Введите размер шахматной доски (NxN), где N - число от 0 до 20: ")

if size.isdigit() and int(size) <= 20:
    size = int(size)
    asc = st.ascii_lowercase[:size]
    for i in range(size, 0, -1):
        for char in asc:
            print(f'{char + str(i): >3}',end=" ")
        print()
else:
    print("Введите корректный размер доски")

# Variant 2
import string as st

n = int(input("In: "))

if n < 0 or n > 20:
    print("Размер доски должен быть от 0 до 20")
else:
    letters = st.ascii_lowercase[:n]
    for num in range(n):
        row = ""
        for char in letters:
            row += f"{char}{n - num} "
        print(row)

    # Variant 3
    import string

    size = input("Введите размер шахматной доски (NxN), где N - число от 0 до 20: ")

    if size.isdigit() and int(size) <= 20:
        n = int(size)
        asc = string.ascii_lowercase[:n]
        for i in range(n, 0, -1):
            for char in asc:
                print(f'{char}{i}'.ljust(len(size) + 1), end=" ")
            print()
    else:
        print("Введите корректный размер доски")