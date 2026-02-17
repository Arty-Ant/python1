# =================
# Условный оператор
# =================

# Шаблон
# if выражение(True):
#     Блок инструкций 1
# elif условие верно:
#     Блок инструкций 2
# elif условие верно:
#     Блок инструкций 3
# elif условие верно:
#     Блок инструкций 4
# elif условие верно:
#     Блок инструкций 5
# else:
#     Блок инструкций 6

# Пример 0
# data = int(input('Enter a value: '))
# if data > 0:
#     print('Число положительное.')
#     print('second line')
# elif data < 0:
#     print('Число отрицательное.')
# else:  # elif data == 0:
#     print('Это нуль.')
#
# print('Done')

# Пример 1 (вложенный if)
# data = int(input('Enter a value: '))
# if data > 0:
#     print('Число положительное')
#     if data > 9:
#         print('Число не однозначное')
# elif data < 0:
#     print('Число отрицательное')
# else:  # elif data == 0
#     print('Число равно 0')
# #
# print('Done')

# ==================
# Операции сравнения
# ==================
'''
== равно
!= не равно
<  меньше
<= меньше или равно
>  больше
>= больше или равно
in входит в объект  # множественное сравнение
not in не входит в объект
'''
# Пример 2
# string = 'Hello'
# print('a' in string)       # Out: False
# print('el' in string)       # Out: True
# print('El' in string)       # Out: False
# print('lol' not in string)  # Out: True
# print('hel' in string)      # Out: False  h != H

# =======================
# Truthy and falsy values
# =======================
# data = '!'  # Пустая строка  Falsy value
# print(len(data))  # len - длина строки (length)
# =======================================================================
# Если data равно 0, 0.0 или пустой строке, то значение выражения - False
# Если data не равно 0 или в data есть хоть один символ, то - True
# =======================================================================
# if data:   # if len(data) != 0:  if bool(data):
#     print('Строка непустая')
# else:
#     print('Строка пустая')

# Функционал тот же, но тяжелее читать код
# if not data:   # if len(data) == 0:
#     print('Строка пустая')
# else:
#     print('Строка непустая')


# Логические операторы not, and, or в порядке приоритета
# n = int(input('Enter a number(1-100): '))
# m = int(input('Enter a number(1-100): '))
#
# # Логическое 'И'
# if n > 0 and m < 100:  # True and True -> True
#     print('Первая проверка пройдена')
#
# # Логическое 'ИЛИ'. Ленивый оператор
# if n > 0 or m < 100:  # True or False -> True; False or True -> True, True and True -> True
#     print('Вторая проверка пройдена')

# Пример ленивого оператора
# if len('hello') > 5 or 1 / 0 > 0:
#     print('work or not')


# # Можно использовать цепочки сравнений
# a = 15
# if 10 < a < 20:  # 10 < a and a < 20
#     print('a is good')
# else:
#     print('a is bad')


# Тернарный оператор (syntax sugar)
# a = 1000
# b = 999
#
# if a > b:
#     print('a bigger than b')
# else:
#     print('b bigger than a or equal')

# Верни а, если а > b это True, иначе верни b
# result = a if a > b else b # a если True иначе b
# print('result: ', result)
# print(a if a > b else b)
# print('a больше b') if a > b else print('a не больше b')
# print('a больше b' if a > b else 'a не больше b')
#
# a = 100
# b = 999
# # Можно, но не рекомендую. Вложенные тернарники
# res = a if a == b else a + 100 if a == 100 else 1
# print(res)  # Out: Вспомнить всё и проверить
#
# # Для читаемости кода нужно сделать так:
# if a == b:
#     res = a
# else:
#     if a == 100:
#         res = a + 100
#     else:
#         res = 1
# print(res)
