# Именование переменных(naming) PEP8:
# верхний регистр, нижний регистр, _, цифры
# Python - регистрозависимый язык!

# Можно, но не нужно
# переменная = 4
# print(переменная)

# Проверка того, что файл в кодировке utf8
# 你好 = 5
# print(你好)


# # Стараемся использовать английский для переменных
# example_value_read = 5
# print(example_value_read)
#
# # Меняем значение на другое(другой тип данных)
# example_value_read = "hello"
# print(example_value_read)
#
# # Пример_константы по соглашению
# LANG = "Python"  # LANG -> константa
# print(LANG)
#
# # можно присвоить другое значение, но это плохой код!
# LANG = 'Java'
# print(LANG)
#
#
# # Создание строк - 4 способа
# first_method = 'Hello'
# second_method = "Python"
# print(first_method)
# print(second_method)
#
# # Используем экранирование
# example_one = 'I\'m Python'
# print(example_one)
# example_second = "I'm Python"
# print(example_second)
# example_third = 'some "values".'
# print(example_third)
#
# # Пример многострочной переменной(multiline string)
# third_method = '''Пример
# многострочного
# комментария'''
# print(third_method)
# fourth_method = """ Строка,
#   которая
#  переходит
# на новые строки.
# """
# print(fourth_method)
#
# example_string = """И "кавычки" и 'апостроф'. """
# print(example_string)
#
# # Это одна строка(one line), но мы используем '\' для продолжения.
# string = 'example of several \
# lines \
# third line.'
# print(string)
#
# # Это одна строка(one line), но мы используем () для продолжения.
# s = ('example too'
#      " long string")
# print(s)
#
# # Конкатенация строк (сложение строк)
# print('hello' + ' ' + 'python')  # Out -> 'hello python'

# Функция type для определения типа переменной
# string = 'example'
# print(type(string))

# Целые числа, тип int
# a = 5
# print(type(a))

# Это возможно
# print(int('5343'))
# print(int('5343') + 1)

# 16-ричная система
# print(int('8787af', base=16))  # Добавляются abcdef
# print(8 * 16 ** 5 + 7 * 16 ** 4 + 8 * 16 ** 3
#       + 7 * 16 ** 2 + 10 * 16 ** 1 + 15 * 16 ** 0)

# Это вернет ошибку
# print(int('11a'))
# print('1' + 1)

# Дробные числа, тип float. Только точка
# c = 5.1
# print('c =', c)
# print(type(c))
#
# d = 5,2  # Только точка, иначе создается кортеж
# print(type(d))
#
# print(float('5.1'))
# print(float('.1'))  # work
# print(float('-.1'))  # work
#
# # Complex number
# comp = 4 + 5j
# print(type(comp), comp)

# Тип Bool
# arg_one = True
# arg_second = False
# print(type(arg_one), arg_one)
# print(type(arg_second), arg_second)
# print('Истинные значения:')
# print(bool('hello'))  # Truthy value
# print(bool(' '))
# print(bool(123.12))
# print(bool(-5))
# print(bool(0.0000000000000000000000000000000001))
# print('Ложные значения:')
# print(bool(0))        # Falsy value
# print(bool(0.0))
# print(bool(''))
# # ЗУ С
# print(True + True + True)  # Out -> 3

# == это равенство
# a = 5
# c = 5.1
# result = type(c) == float # bool
# print(result)
# print(type(c) == float)
# result_1 = a > c
# print(result_1)

# ===========
# Ввод данных
# ===========
# print('Введите данные: ')
# data = input()  # Всегда вернется строка!!!
# print(data, type(data))
# number = input('Enter first number: ')
# print(type(number))  # 'str'
# number = int(number) # str -> int
# print(type(number), number + 1)

# Если мы хотим сразу получить int, то можно делать так:
# message = "Enter second number> "
# num = int(input(message))
# print(num, type(num))

# Если сильно нужно использовать тип данных в имени
# float_ = float(input("Enter third number: "))
# print(float_, type(float_))

