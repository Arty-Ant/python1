# ========================================
# ## Кортежи - Неизменяемые списки(tuples)
# ========================================
# a = 4, 1  # Скобки не обязательно
# print(a, type(a))
#
# b = (3, 5, 'hello', 9, True, 9)
# print(f'{b = }')
#
# c = tuple('hello,python, java')
# print(f'{c = }')

# Создание кортежа из одного элемента
# one = 1,
# print(one)
# one_again = ('hello',)
# print(one_again, type(one_again))

# функции кортежа: count() и index()
# print(b.count(9))    # Out: 2
# print(c.count('o'))  # Out: 2
# print(b.index(5))    # Out: 1

# из кортежа в список и из списка в кортеж
# lst = list(b)
# print(f'{lst = }', type(lst))
# new_tuple = tuple(lst)
# print(f'{new_tuple = }', type(new_tuple))

# new_tuple[0] = 999  # Error

# ============
# Pythonic way
# ============

# Функция enumerate пронумеровывает последовательность
# как замена конструкции for idx in range(len(lst)): ...
# ## Пример 1
# from random import randint
#
# lst = []
# for _ in range(20):
#     lst.append(randint(10, 15))
# print(f'{lst = }')
#
# need_indexes = []
# for index, value in enumerate(lst):
#     if value == 14 or value == 12:
#         need_indexes.append(index)
#     if value == 15:
#         lst[index] = 100
# print(f'{need_indexes = }')
# print(f'{lst = }')
#
# # каждый элемент - кортеж
# for item in enumerate('hello'):
#     print(item)
#
# # Происходит распаковка кортежа
# for index, value in enumerate('hello'):
#     print(f'{index}: {value}')
