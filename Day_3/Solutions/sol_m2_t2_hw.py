"""
Задача №1
По заданному числу n определите нужное окончание слова "бутыл?"
Одним из возможных вариантов будет: «n бутылок», «n бутылка», «n бутылки», 
Число n от 0 до 5000.

Пример:
In: 10
Out: 10 бутылок

In: 24
Out: 24 бутылки
"""
# Variant 1
bottle_count = int(input('Введите число бутылок от 0 до 5000: '))

last_num = bottle_count % 10                    # находим последнюю цифру числа
second_last_num = bottle_count % 100            # находим 2 последних цифры числа

if 11 <= second_last_num <= 14:                 # отсекаем исключения
    print(f'{bottle_count} бутылок')
else:
    if last_num == 1:
        print(f'{bottle_count} бутылка')
    elif 2 <= last_num <= 4:
        print(f'{bottle_count} бутылки')
    else:
        print(f'{bottle_count} бутылок')

# Variant 2
s = input("Введите количество бутылок (0-5000): ")

if not s.isdigit():
    print("Это неверное число")
else:
    num = int(s)
    if num < 0 or num > 5000:
        print("Это неверное число")
    else:
        remainder10 = num % 10
        remainder100 = num % 100
        if 11 <= remainder100 <= 14:
            suffix = "ок"
        elif remainder10 == 1:
            suffix = "ка"
        elif 2 <= remainder10 <= 4:
            suffix = "ки"
        else:
            suffix = "ок"

        print(f"У вас {num} бутыл{suffix}")

# Variant 3
bottle = input('Введите количество бутылок: ')

if 0 <= int(bottle) <= 5000 :
    if ( int(bottle[-1]) == 0 ) or ( 5 <= int(bottle[-1]) <= 9 ):
        print(f'{bottle} бутылок')
    elif int(bottle[-1]) == 1 :
        if len(bottle) >= 2 and int(bottle[-2]) == 1:
            print(f'{bottle} бутылок')
        else:
            print(f'{bottle} бутылка')
    elif bottle[-1] in '234' :
        if len(bottle) >= 2 and int(bottle[-2]) == 1:
            print(f'{bottle} бутылок')
        else:
            print(f'{bottle} бутылки')
else:
    print('Число находится не в диапазоне от 0 до 5000')

# Variant 4
num = input('Введите число от 0 до 5000: ')
if not 0 <= int(num) <= 5000:
    print('Ваше число не входит в заданное множество чисел')

elif int(num[-1]) == 0 or 11 <= int(num[-2:]) <= 14 or 5 <= int(num[-1]) <= 9:
    print(f'{num} бутылок')

elif int(num[-1]) == 1:
    print(f'{num} бутылка')

elif 2 <= int(num[-1]) <= 4:
    print(f'{num} бутылки')