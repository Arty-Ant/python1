"""
Задача:
Проверить, является ли четырехзначное число палиндромом
Пример:
Вход: 1221  Выход: 1221 - палиндром
Вход: 1234  Выход: 1234 - не палиндром
"""
# num = input("Enter data> ")
# print(num, type(num) == str, len(num))

# Положительные индексы начинаются с нуля и добавляют 1
# Слева направо
# if num[0] == num[3] and num[1] == num[2]:
#     print('Палиндром')
# else:
#     print('Не палиндром')

# Отрицательные индексы начинаются с -1 и добавляют -1
# Справа налево
# if num[-4] == num[-1] and num[-3] == num[-2]:
#     print('Палиндром')
# else:
#     print('Не палиндром')

# Срезы(slice)
# Шаблон -> [start:stop:step]
# start - начальный индекс, по умолчанию равен 0, если step равен +1
# stop - индекс, на котором мы останавливаемся, его значение не включается
# step - шаг в интервале значений, по умолчанию равен +1
# start, stop, step могут быть положительными и отрицательными
#
string = 'Hello, Python'
# 2, 3, 4
print(string[2:5])    # Out -> 'llo'
print(string[2:5:1])  # Out -> 'llo'

# 0, 1, 2, 3, 4, 5
# Первые шесть элементов последовательности
print(string[:6])  # Out -> 'Hello,'
print(string[0:6:1])

# 5, 7, 9
print(string[5:10:2])  # Out -> ',Pt'

# Последние шесть элементов последовательности
# -6, -5, -4, -3, -2, -1
print(string[-6:]) # start index = -6
print(string[-6::1])

# Отрицательный шаг
print(string[-3:-6:-1])  # [-3], [-4], [-5]
print(string[10::-1])

# Можно использовать одновременно
print(string[-6:10])  # ! string[10] == string[-3]

# Важное отличие от взятия индекса, например: string[100]
print(string[8:100])  # ошибки не будет
print(string[30:40])  # ошибки не будет -> Out: ''
print('Выше пустая строка')

# Разворот строки(reverse)
print(string[::-1])

string = 'hello, ,olleh'
if string == string[::-1]:
    print('good')
else:
    print('bad')

# =============
# функции строк
# =============
# # Пример 1 неотрицательные числа
# data = input('Enter a string: ')
# # Вернут True, если в строке только цифры
# if data.isdigit():   # Тоже самое, что: data[i] in '0123456789'
#     print('All good', int(data) + 1)
# else:
#     print("Bad data")

# # Пример 2 отрицательные числа
# data = input('Enter a string: ')
# # Вернут True, если в строке только цифры
# if data[0] == '-' and data[1:].isdigit():
#     print('All good', int(data))
# else:
#     print("Bad data")

# # Работа с индексами
# data = '1234529'
# # Если элемента нет, то функция str.index() выдаст ошибку
# # Вернет индекс элемента('2')
# if '2' in data:
#     print(data.index('2'))

# # Пример получение следующего индекса для одного и того же значения
# s = 'hello ol ho'
# first_i = s.index('o')
# print(first_i)  # 4
# if 'o' in s[first_i + 1:]:
#     print(s.index('o', first_i + 1))  # 6

# # Если элемента нет, то функция str.find() вернет -1
# print(s.find('llo')) # 2
# print(s.find('lol')) # -1

# data = input('Enter a data: ')
# # Удаляем пробельные символы в начале и в конце строки
# print(f'start:{data.strip()}:finish')

# # Удаляем пробельные символы только в начале строки
# print('start:', data.lstrip(), 'finish')
# #
# # Удаляем пробельные символы только в конце строки
# print('start:', data.rstrip(), 'finish')

# # !Важный момент работы функции strip()
# data = 'oa!выкинул!oouooo'
# print('start:', data.strip('oau!'), ':finish')

# Замена одной подстроки на другую
# string = 'saaaah  aasotuhaaas  aa'
# before_id = id(string)
# string = string.replace('aa', '!')  # Out -> s!!h  !sotuh!as  !
# print(string)
# print(before_id == id(string)) # Вспомнить и проверить!


# Полезные константы из модуля string
# Импортируем модуль как переменную st
# import string as st


# print(st.ascii_lowercase)  # abcdefghijklmnopqrstuvwxyz
# print(st.ascii_uppercase)  # ABCDEFGHIJKLMNOPQRSTUVWXYZ
# print(st.digits)           # 0123456789
# print(st.punctuation)      # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# print(st.hexdigits)        # 0123456789abcdefABCDEF
# print(st.ascii_letters)    # abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ







