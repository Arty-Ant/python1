"""
Задача №2
Дано натуральное число N. Если число N двузначное,
то найти сумму цифр числа. Если число N трехзначное,
то найти произведение ненулевых цифр числа,
иначе написать, что число неподходящее.

Если в 3-х значном и десятки и единицы нули, то выводим только сотни.

Цикл while не используем!
Можно работать с числом как со строкой.

In: 300
Out: 3

In: 405
Out: 20

In: 230
Out: 6

In: 67
Out: 13

In: 6
Out: 'число неподходящее'

In: 5678
Out: 'число неподходящее'
"""
# Variant 1
s = input("Введите 2-х или 3-х значное число: ")
if not s.isdigit() or len(s) < 2 or len(s) > 3:
    print("Это неверное число, введите снова")
else:
    s = str(int(s))
    if len(s) == 2:
        result = int(s[0]) + int(s[1])
    else:
        if s[1:] == "00":
            result = s[0]
        else:
            result = int(s[0]) * (int(s[1]) if s[1] != "0" else 1) * (int(s[2]) if s[2] != "0" else 1)

    print(result)

# Variant 2
number = input('Введите число: ')

if 0 < len(number) < 4:
    if len(number) == 2:
        summa = int(number[0]) + int(number[1])
        print(f'Сумма: {summa}')
    elif len(number) == 3:
        if int(number[0]) and int(number[1]) and int(number[2]) == 0:
            mult = int(number[0]) * int(number[1])
            print(f'Умножение: {mult}')
        elif int(number[0]) and int(number[1]) == 0 and int(number[2]) == 0:
            mult = int(number[0])
            print(f'Умножение: {mult}')
        elif int(number[0]) and int(number[1]) == 0 and int(number[2]):
            mult = int(number[0]) * int(number[2])
            print(f'Умножение: {mult}')
        elif int(number[0]) and int(number[1]) and int(number[2]):
            mult = int(number[0]) * int(number[1]) * int(number[2])
            print(f'Умножение: {mult}')
else:
    print('число неподходящее')

# Variant 3
num = input("Введите любое двухзначное или трёхзначное число: ")
qty = len(num)
if qty == 2:
    print((int(num) // 10) + (int(num) % 10))
elif qty == 3:
    if '00' in num:
        print(num[0])
    elif num[1] == '0':
        print(int(num[0]) * int(num[2]))
    elif num[2] == '0':
        print(int(num[0]) * int(num[1]))
    else:
        print(int(num[0]) * int(num[1]) * int(num[2]))
else:
    print(f"Число {num} неподходящее")

# Variant 4
num = input('Введите натуральное двузначное или трехзначное число: ')

if not 2 <= len(num) <= 3:
    print('число неподходящее')

elif len(num) == 2:
    sym_1 = int(num[0])
    sym_2 = int(num[1])
    summa = sym_1 + sym_2
    print('Сумма цифр двузначного числа:', summa)

elif len(num) == 3:
    sym_1 = int(num[0])
    sym_2 = int(num[1])
    sym_3 = int(num[2])

    if sym_1 == 0:
       sym_1 = 1
    if sym_2 == 0:
       sym_2 = 1
    if sym_3 == 0:
       sym_3 = 1

    multi = sym_1 * sym_2 * sym_3
    print('Out:', multi)

# Variant 5
n = int(input("Number: "))

if 10 <= n <= 99:
    print(sum(divmod(n, 10)))  # n // 10 + n % 10
elif 100 <= n <= 999:
    a = n // 100     # Сотни
    b = n // 10 % 10 # Десятки  0 vs 1,...,9
    c = n % 10       # Единицы  0 vs 1,...,9

    print(a * b ** bool(b) * c ** bool(c))
else:
    print("Число неподходящее.")


# Variant 5
number = int(input("Введите число:"))
if 10<= number <= 99:
    stroka = str(number)
    num_1 = int(stroka[0])
    num_2 = int(stroka[1])
    summa = num_1 + num_2
    print(summa)
elif 100 <= number <= 999:
    stroka = str(number)
    num_1 = int(stroka[0])
    num_2 = int(stroka[1])
    num_3 = int(stroka[2])

    if num_2 and num_3:
        print(num_1 * num_2 * num_3)
    elif num_3:
        print(num_1 * num_3)
    elif num_2:
        print(num_1 * num_2)
    else:
        print(num_1)
else:
    print('число неподходящее')