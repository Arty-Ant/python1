# ======================
# Форматированные строки
# ======================
name = 'Stepan'
age = 20

# Параметры sep(по умолчанию ' ') и end (по умолчанию '\n')
# print(name, age, name, age, sep='|', end=' the_end_of_string ')
# print('Новая строка')
# print("Здравствуйте, ", name, ".", sep='', end=' ')
# print("Вам", age, "лет.")

# 1-й способ - это %
# print('Result of our program %s and %s. Two values.' % (name, age))
# print('Result of our program %s. First value.' % name)  # одна переменная
# print('Result of our program %s and %i. Two values.' % (name, age))
# # Вывод переменной с типом float
# # с ограничением в 3 разряда после точки
# print('Result of our program %.3f !!! First value.' % (age / 3))

# 2-й способ - функция format
# print('Your name is {}. You are {}.'.format(name, age))
# in_str = 'You are {1}. Your name is {0}.'
# out_str = in_str.format(name, age)
# print(out_str)
# print('You are {1}. Your name is {0}.'.format(name, age / 3))
# # # Можно подставлять и выражения (Что(Индекс): КАК отформатировать)
# print('You are {1:.3f}. Your name is {0}.'.format(name, age / 3))
# print('You are {1:10.2f}. Your name is {0}.'.format(name, age / 3))

# 3-й способ - f-string (f или F перед строкой. Разницы нет)
# print(f'Your name is "{name}". You are {age}.')

# Можно подставлять и выражения (ЧТО(имя переменной): КАК отформатировать)
# print(f'Your name(three times) is{(" " + name) * 3}. You are {age / 3:.2f}.')

# Задача про обратное число
# num = int(input('Введите 3-х значное число: '))
# result = F'Обратное число: {num % 10}{num // 10 % 10}{num // 100}'
# print(result)

# Синтаксический сахар
# print(F"{age = }")     # То же самое: print(f'age = {age}') # Out -> age = 10
# print(f'age = {age}')  # the same


# https://docs.python.org/3/library/string.html#formatstrings

# ========
# Примеры:
# ========
# a = 230
# b = 32
# # Заполнить ведущими нулями
# print(str(b).zfill(3))
#
# c = 45.5
# d = 0.75
#
# # символ '>' это смещение вправо.
# print(f'{b:0>3}')
# print(f'{c:0>10.2f}')
#
# # символ '<' это смещение влево.
# print(f'{c:x<8}')
#
# # символ ',' или '_' это разделение разрядов.
# print(f'{1234567:10,}') # 10 позиций с учетом <,>
# print(f'{1234567:,}')
# print(f'{1234567:_}')
#
# # символ '%' это умножение на 100 и
# # добавление знака процента.
# result = f'{d:.1%}' + ' '
# print(result * 2)
#
# # Перевод в base=2 или base=16
# print(f'{21:x}')  # base=16
# print(f'{21:b}')  # base=2
#
# # Часть возможностей можно использовать вместе
# e = 12345
# print(f'{e:0>7,}')
# f = 1234.87373
# print(f'{f:_.1%}')
#
# alfa = 'abc'
# # по центру
# print(f':{alfa:^9}:')
# print(f'|{alfa:^9}|{'abcde':^9}|{'cdf':^9}|')