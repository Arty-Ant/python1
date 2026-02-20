# =====================================
# Словари (dict), изменяемый тип данных
# структура: key(ключ): value(значение)
# =====================================

# До этого - работа с индексами, теперь с ключами
# s = 'hello, students'             # это строка(str)
# lst = [3, 8, 4.1, 'hello', True]  # это список(list)
# t = (3, 89, 6.1, 'python', False) # это кортеж(tuple)
# r = range(20)                     # это прогрессия(range)

# balls colors
# red
# blue
# yellow
# green
# Неудобно запоминать значения через индексы
# balls_lst = [5, 7, 11, 10]

# # Словари, тип данных(ключ: значение)
# ## !!! Словари - это ключи !!!
# # Ключи словарей - это только неизменяемые типы данных:
# # str, int, float, bool, tuple, range
# # Ключи словаря - это уникальные значения(нет повторяющихся)
# # Значения словаря - это любые типы данных
# модуль pretty print для красивого(вертикального) вывода
# import pprint
#
# balls = {'red': 5, 'blue': 7, 'yellow': 11, 'green': 10}
# print(balls)
# print(type(balls))  # dict
#
# # Обращение к значению по ключу словаря
# print(balls['red'])  # как читать значение
#
# # ## Важно это запомнить!
# # Создание пары или изменение значения ключа
# # Если такой ключ есть в словаре, то меняем значение у этого ключа
# # Если такого ключа нет, то создаем новую пару.
# balls['red'] = 12  # как создать либо поменять значение
# print(balls)
#
# # Как изменить значение?
# balls['blue'] = balls['blue'] - 7
# balls['green'] -= 7  # такая же операция, только используя -=
# balls['yellow'] = 33
#
# # Проверка. Изменился или нет
# print(balls)
#
# # Если ключа нет - будет ошибка
# # print(balls['black'])  # KeyError: 'black'
#
# # ## Как добавить пару(ключ: значение)
# balls['black'] = 10
#
# # Красивый(вертикальный) вывод
# pprint.pprint(balls, width=20, sort_dicts=False)
#
# # Как проверить существуют ли ключ в словаре?
# print('pink' in balls)
# print('pink' not in balls)
# print('red' in balls)
# print('red' not in balls)
#
# # Получение значения через функцию get()
# print(balls.get("red", "Нет такого ключа"))
# print(balls.get('pink', "Нет такого ключа"))
#
#
# # Вместе с if и in
# color = 'white'
# if color not in balls:
#     balls[color] = 1
# else:
#     balls[color] += 1  # balls['white'] = balls['white'] + 1
#
# # Красивый(вертикальный) вывод словаря
# pprint.pprint(balls, width=20)
# print('=' * 30)
#
# if 'red' in balls:
#     balls['red'] += 1 # balls['red'] = balls['red'] + 1
# else:
#     balls['red'] = 1
#
# pprint.pprint(balls, width=20)
#
# # Как создать пустой словарь
# d1 = dict()  # пустой словарь, falsy value
# d2 = {}      # пустой словарь, falsy value
# print(d1, d2)
#
# # особенности dict()
# # a1 и hello - это ключи 'a1' и 'hello' в новом словаре
# d3 = dict(a1=34, hello='python')
# print(d3)

# ===============================
# Словари с разными типами ключей
# ===============================
# dict_a = {
#     1: 23,
#     'Март': 8.123,
#     8.2: 'hello',
#     (1, 'lang'): 'python'
# }

# print(dict_a)
# print(dict_a.keys())
#
# # Пройтись по всему словарю, т.е. по всем ключам словаря
# for key in dict_a:
#     # Тоже самое, можно без keys()
#     # for key in dict_a.keys():
#     print(f'{key}: {dict_a[key]}')

# =================
# Функции словарей.
# =================

## dict.keys() - это ключи
# print(dict_a.keys())
#
# # ## dict.values() - это значения
# print(dict_a.values())
# vals = dict_a.values()
# print(f'{vals = }', type(vals))
# # Явно меняем на список
# print(list(vals)[0])
# print(tuple(dict_a.keys())[2:4])  # Out: (8.2, (1, 'lang'))
#
# # Чтобы работать как со списком, нужно привести к списку.
# print(list(dict_a.values())[-1])
#
# # dict.items() - это пары(ключ,значение)
# # Результат - "список кортежей"
# print(dict_a.items())
#
# # Пример использования
# for key, value in dict_a.items(): # key, value = (1, 23)
#     print(key, ': ', value, sep='')
# #
# print('=' * 30)
# for param in dict_a.items():
#     key, value = param
#     print(param)
#     print("repeat:", key, value)
#
# print('=' * 30)
# for param in dict_a.items():
#     print(*param, sep=': ') # распаковка кортежа

# =====
#  zip
# =====
# # Как быстро создать словарь с помощью функции zip
# months = 'Март', 'Май', 'Июнь', 'Июль', 'Август'  # tuple
# scores = [  9,    7.1,    8,     23]
# # # Аргумент strict=True требует, чтобы кол-во элементов было равным
# # # по умолчанию равен False
# # total_lst = list(zip(months, scores, strict=True))
# total_lst = list(zip(months, scores))
# total_tup = tuple(zip(months, scores))
# print(f'{total_lst = }')
# print(f'{total_tup = }')
#
# # Получаем словарь на основе списка кортежей
# dict_b = dict(zip(months, scores))  #
# print(dict_b)
# print(len(dict_b))  # Out: Вспомнить и проверить
#
#
# dict_c = dict(total_lst)
# dict_d = dict(total_tup)
#
# print(f'{dict_c = }')
# print('before:')
# print(f'{dict_d = }')
#
# # функция update() обновит словарь dict_d за счет dict_a
# dict_d.update(dict_a)
#
# import pprint
# # Красивый(вертикальный) вывод словаря
# print('Обновленный словарь dict_a')
# pprint.pprint(dict_d, width=20, sort_dicts=False)
# print(dict_d)
#
# # С версии 3.9 можно быстро объединять словари через |
# # и получить новый "общий" словарь
# balls = {'red': 5, 'blue': 7, 'yellow': 11, 'green': 10}
# pprint.pprint(dict_a | balls | dict_c)
# result = dict_a | balls | dict_c
# pprint.pprint(result)
# new = dict_a + dict_c  # error

# ==================
# Удаление элементов
# ==================
# dict_a = {
#     1: 23,
#     '2': 8.1,
#     8.2: 'hello',
#     (1, 'lang'): 'python',
# }
#
# import pprint
# # По ключу удаляем пару и возвращаем значение
# pprint.pprint(dict_a, sort_dicts=False)
# del_value = dict_a.pop(1)  # 1 - это ключ и мы получаем значение удаленного ключа
# print(del_value)
# print(dict_a)
# #
# del_value = dict_a.pop('2')
# print(del_value)
# print(dict_a)
#
# # Удаляем пару и возвращаем кортеж(ключ, значение)
# del_item = dict_a.popitem()
# print("last element:", del_item)
#
# print(f'{dict_a = }')

# ===============
# Сложные словари
# ===============
# first = {
#     'July': (9, 8, 2, 1),
#     'June': (7, 9, 8.1, 2),
#     'March': (8, 7, 11, 3)
# }
#
# print(first['July'][0])  # Out: 9
#
# second = {
#     2: (9, 8, 2, 1),
#     6: (7, 9, 8.1, 2),
#     7: (8, 7, 11, 3)
# }
#
# print(second[2][2])  # Out: 2

