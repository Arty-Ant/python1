# ===============
# Вложенные циклы
# ===============
# Variant 1
# counter = 0
# for i in range(5):  # range(0, 5, 1)
#     print(f'Начинаю работу вложенного цикла в {i + 1}-й раз: ')
#     for j in range(4): # range(0, 4, 1)
#         counter += 1
#         print(f'{i = }, {j = }', end=' | ')  # Сколько раз?
#     print()
#
# print(f'{counter = }')  # 20


# Variant 2
# time = 0
# for i in range(5):      # 0, 1, 2, 3, 4
#     for j in range(4):  # 0, 1, 2, 3
#         if i + j > 5:
#             break
#         time += 1
#         # Сколько раз?
#         print(f'{i = }, {j = }', end=' | ')
#     print()
# print()
# print(f'{time} раз') # 17



# Variant 3
# for i in range(5): # 0, 1, 2, 3, 4
#     j = 0
#     while i + j < 5: # 0+0, 0+1, 0+2, 0+3, 0+4
#         # Сколько раз выполнится print()? 15
#         print(f'{i = }, {j = }', end=' | ')
#         j += 1
#     print()



# КВ Variant 4
# s = 'program'
# index = time = 0
# while index < len(s):  # 0, 1, 2, 3, 4, 5, 6
#     if index % 2:   # index = 1, index = 3, index = 5
#         for char in s:  # Сколько итераций(количество повторений цикла): 7
#             time += 1
#             # Сколько раз ?
#             print(f'{time = }: {char.upper()}', end=' ')
#         print()
#     index += 1
#
# print(f'Check: {time}')  # 21
# print(f'{index = }')     # 7


# КВ Variant 5
# time = 0
# for i in range(4):
#     time += 1 # 4 x 1 = 4
#     for j in range(3):
#         time += 3  # 12 x 3 = 36
#     time -= 2  # 4 x (-2) = -8
#
# print(time)  # 32


