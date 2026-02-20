# ==============================
# Изменяемый тип данных - Списки
# ==============================

# ================
# Создание списков
# ================
# a = [1, 2, 'hello', 8.3, True]
# print(type(a))
# print(a)
#
# b = []      # Пустой список, Falsy value
# print(b, type(b))
#
# # list() принимает только один аргумент и этот
# # аргумент должен быть последовательностью
# c = list()  # Пустой список, Falsy value
# print(c, type(c))
# #
# # # Функция list принимает только один аргумент
# lst = list(range(11))
# print('lst: ', lst)
#
# lst_new = list('hello')
# print(f'{lst_new = }')
#
# # Итерирование по списку (Просто считываем)
# for item in a:
#     print(item)
#
# print(f'{item = }')  # Out: True
#
# print('Before change. id of a: ', id(a))
# print('Доступ по индексу')
# # Изменение значений элементов списка
# for index in range(len(a)):  # a = [1, 2, 'hello', 8.3, True]
#     # Изменяем значение элементов списка
#     a[index] = index
#
# print(f'{a = }')  # f'a = {a}'  Out: [0, 1, 2, 3, 4]
# print('After change. id of a: ', id(a))

# Можно в список класть переменные
# b = 5
# c = 'hello'
# d = 8.2
# lst_2 = [b, c, d]
# print(f'{lst_2 = }')

# # функция split() разделяет строку на элементы по пробельным символам
# b = input('Enter data: ').split()  # b - это список строковых значений
# print(type(b), b)
# for i in range(len(b)):
#     if b[i].isdigit():
#         # Меняем значения элементов списка
#         b[i] = int(b[i])
#     else:
#         # значение None('ничего'), falsy value
#         b[i] = None
#
# print(f'after: {b = }')
# print(len(b))
#
# # Меняем значение None в списке на ноль
# for index in range(len(b)):
#     # В этом случае используем оператор is
#     if b[index] is None:
#         b[index] = 0
#
# print('new b', b)
# print(sum(b))


# Работа с индексами в списке
# lst = [3, 6, 8.2, ['hello'], True, 'one']
# print(lst[3], type(lst[3]))  # list
# print(lst[3][0])      # 'hello'
# print(lst[3][0][-1])  # 'o'
# print(lst[3][-1])     # 'hello'
# print(lst[3][0][4])   # 'o'
# print(lst[-1][0])     # 'o'
# print(lst[3][0][-2:])  # 'lo'
# print(lst[:2])
# # print(lst[3][1][-1])  # Error
# print(lst[3][0][1])


# Изменение списка через срезы
# lst2 = list(range(10))
# print('Before:', lst2)
# lst2[2:6] = [99, 98, 97, 96, 95, 94]
# print('After:', lst2)
# lst2[2:8] = [100]
# print('After:', lst2)
# # lst2[2:5] = []
# # print('After:', lst2)
# # !!!! Кол-во заменяемых элементов должно совпадать
# lst2[2:5:2] = [99, 999]
# print('After:', lst2)
# lst2[2:3] = '100'  # неявно list('100')
# print('After:', lst2)

# ===============
# Функции списков
# ===============
# a = [1, 2, 'hello', 8.3, True]
# print(f'{a = }')
# # добавление элемента в конец списка только одного элемента
# a.append(5)
# print('list a:', a)

# Пример для list.append()
# result = []  # пустой список
# s = 'HelloStudents'
# counter = 0
# vowels = ['a', 'o', 'e', 'u', 'i']
# for char in s:
#     if char in vowels:
#         counter += 1
#     else:
#         result.append(char)
#
# print(F'{counter = }')  # кол-во гласных
# print(f'{result = }')   # список согласных
#
# # Собираем из списка строковых значений одну строку
# s1 = ''.join(result)
# print('s1: ', s1)

# Делаем копию списка с другим id
# a = [1, 2, 'hello', 8.3, True]
# print(f'{a = }')
# ## Первый вариант
# print(id(a))
# n = a[:]  # срез(слайс) всех элементов
# print(id(n))
# a[0] = 111
# print(f'{a = }')
# print(f'{n = }')
# print(a is n)  # False
#
# Второй вариант
# b = a.copy()
# print(f'{b = }')
# a[0] = 99
# print(f'{a = }')
# print(f'{b = }')
# print(a is b)  # False

# # ## Выводит количество вхождений элемента в список
# print(a.count('hello'))  # 1
# print(a.count(True))    # Out: 2 -> 1 == True
# print(a.count(1))       # Out: 2
# # print(a.count())  # TypeError: list.count() takes exactly one argument (0 given)
#
# ## Индекс элемента в списке
# print(f'index of 2 is {a.index(2)}'
#       f' and index of True is {a.index(True)}')
#
# # ## Увеличивает список за счет другого списка
# a.extend([10, 11])
# print('list a: ', a)


# ========================
# Удаление элемента списка
# ========================
# a = [1, 2, 'hello', 8.3, True]
# ## Удаляем последний элемент, если не указан индекс
# print(f'a before a.pop(): {a}')
# a.pop()  # a.pop(-1)
# print(f'a after a.pop(): {a}')
#
# # ## можем удалить элемент с указанным индексом
# # del_item = a.pop(2)
# # print('del_item - {}'.format(del_item))
# # print(a)
#
#
# # ## удаляем первый элемент(слева) по значению,
# # ## ошибка если элемента нет в списке
# a.extend([10, 11])
# print('list a: ', a)
#
# a.remove(10)
# print(a)
#
#
# # Разворачиваем список
# a.reverse()  # a[::-1]
# print('a after reverse:', a)
#
#
# # ## Сортировка по возрастанию
# a.pop(a.index('hello'))
# a.sort()
# print("a after sorting:", a)
#
# # Сортировка по убыванию
# a.sort(reverse=True)
# print(a)
#
#
# # ## Используем лексикографическую сортировку
# lst = ['hi', 'hoho', 'python', 'Hello']
# lst.sort()
# print(lst)  # Out: ['Hello', 'hi', 'hoho', 'python']
#
# ## Вставка элемента на определенный индекс
# print(f'before: {a = }')
# # ## 2 это индекс для вставки значения 'some value'
# a.insert(2, 'some and value')
# print(f'after: {a = }')
#
# ## Метод clear
# c = a.copy()
# print('list c: ', c)
#
# ## Очищаем список от значений. Результат - пустой список
# c.clear()
# print('list c: ', c)

# ===================
# Операция распаковки
# ===================
# a = [1, 2, 'hello', 8.3, True]
# print(a)
# print(*a, sep='|')  # * это операция распаковки
# print(a[0], a[1], a[2], a[3], a[4])

# # medium всегда список и он может быть пустым.
# first, *medium, last = 'hello'
# print(f'{first = }')
# print(f'{medium = }') # это список
# print(f'{last = }')
# _, _, third, *medium, last = a  # a - это список
# print(f'{third = }')
# print(f'{medium = }')
# print(f'{last = }')


# ## Удаление элемента с помощью del
# print("before del:", a)
# del a[-2]
# print("after del:", a)
#
# # ## Удаление переменной(объекта) целиком
# del a
# print(a)  # NameError: name 'a' is not defined

# ===========================
# Обработка вложенных списков
# ===========================
## Создаем большой список из других списков
# lst = [4, 9, 12, 3.1, True]
# strings = ['hello', 'python', 'well', 'done']
# res = [8.2, 9, 4, 7, False]
#
# big_list = [lst, strings, lst, res]
# print(f'{big_list = }')
#
# # Внешний цикл проходится по вложенным спискам
# for inner_lst in big_list:
#     print('Очередной вложенный список:')
#     # Этот цикл проходится по элементам очередного списка
#     for item in inner_lst:
#         print(item, ':', len(str(item)))
#         if type(item) == str:
#             for char in item:
#                 print('отдельно символ', char)
#             print()
#     print()
