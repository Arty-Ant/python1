# ===========
# Цикл "for"
# ===========
# =======
# Шаблон:
# =======
# for элемент_последовательности in последовательности:
#     блок инструкций

# Примеры работы for
# greet = 'Hello, world'
# for char in greet:   # char = 'H', char = 'e', char = 'l', ...., char = 'd'
#     print(char.upper(), end=':')
#
# print()
# print(f'{char = }')  # Out: d
#
# # Можно менять строку с помощью срезов и использовать цикл
# for char in greet[:5]:  # 'Hello'
#     print(char, end=' ')
# print()
#
# # Пример подсчета символа в строке
# greet = 'Hello, world'
# counter_l = 0
# for symbol in greet:
#     if symbol == 'l':
#         counter_l += 1  # Считаем количество букву 'l'
#
# print(f'{counter_l = }')
# # Тот же результат с помощью функции str.count()
# print(greet.count('l'))


# Арифметическая последовательность(прогрессия) целых чисел - range()
# range(start, stop, step)
# Начало последовательности, конечное значение и шаг(+, -)
# По умолчанию start = 0, step = 1
# print(range(10), type(range(10)))  # 0, 1, 2, 3, 4, 5, 6, 7, 9
# print(range(0, 10, 1))        # то же самое, что и range(10)
# print(5 in range(5))          # Out: False
# print(12 in range(0, 20, 3))  # Out: True
# print(len(range(12)))
# print(range(21, 31)[4])  # Out: 25
# print(range(10)[2:8])
#
# # Проверяем
# for number in range(0, 20, 3): # number = 0, number = 3, ..., number = 18
#     print(number, end=':')
# print()
#
#
# # Повторение определенного количества раз
# for i in range(5):  # i = 0, i = 1, 2, 3, 4
#     print(f'{i + 1} раз: Hello, Students')
#
# print('*' * 30)
#
# # Без переменной цикла, по соглашению используем _
# counter = 5
# for _ in range(counter): # range(0, 5, 1)
#     print('Hello, Students')
#
# print('*' * 30)
#
# # По соглашению используем _,
# # если нам не нужно само значение переменной цикла
# step = 3
# for _ in range(0, 14, step):  # 0, 3, 6, 9, 12
#     print('Hello, Students')  #
#
#
# # Здесь мы переменную цикла используем
# for item in range(10):
#     print(item, end=' ')
# #
# print()
# print('-' * 20)
#
# Извлекаю квадратный корень из чисел от 4 до 9
# Можно, но не нужно(item)
# for item in range(4, 10):  # item = <очередное значение>
#     print(item ** .5)  # .5 == 0.5
#     item += 10
#     print(f'{item = }')
#
# print('-' * 20)
# print(f'{item = }')


# Сколько чисел на выходе?
# for j in range(-8, 10, 2):  # Out: Вспомнить и проверить
#     if j:                   # Подсказка: truthy and falsy values
#         print('четные: ', j)
# #
# print('-' * 20)
#
# print('Repeat')
# # Пример с continue
# for j in range(-8, 10, 2):
#     if j == 0:  # the same -> if not j:
#         continue
#     print('четные: ', j)
#
# print('-' * 20)
#
# # Отрицательный шаг
# for item in range(10, 0, -1):
#     print(item, end=' ') # 10, ..., 1
# #
# print()

# Пример доступа к значениям с помощью индекса
# реализация расширенной функции str.index(): greet.index('w')
# greet = 'Hewllo, worlwd'
# for index in range(len(greet)):  # Out: 0, 1, ...., len(greet) - 1
#     if greet[index] == 'w':
#         print(f'index of w is {index}')


# # Пример работы break в цикле for и блока else для for
# stop = 1000
# greet = 'Hello wor,ld'
# for index in range(len(greet)):
#     if greet[index] == ',':
#         # Получаем индекс для stop'а
#         stop = index
#         break
# else:
#     print('<,> мы не встретили')
# #
# # Если break выполнился, то else(for) не отработает.
# # Если прерывания с помощью break не было, то else(for) отработает
# #
# # Вывожу строку до запятой
# print(greet[:stop])
