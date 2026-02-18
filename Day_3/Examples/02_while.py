# ============
#  Цикл while
# ============

# =============
# Общий шаблон:
# =============
# Начальное присваивание
# while Верно условие:
#     Тело цикла(инструкции)
#     Изменение условия

# Пример 1
# a = 10
# b = 2
# while b < a:
#     # возведение в степень 2
#     c = b ** 2
#     print(f'{b = }, {c = }')
#     print('=' * 30)
#     b += 1
#
# print('Все посчитано')
# print(f'{b = }')  # Вспомнить и проверить


# Пример 2
# print('======= Пример 2 =======')
# d = 87
# # Цикл будет выполняться до тех, пор пока d - нечетное
# while d % 2:  # Подсказка: неявный bool
#     print('старое значение d:', d)
#     d //= 2  # d = d // 2
#     print('новое значение d:', d)
# #
# print('Итоговое значение: ', d)  # Out: Вспомнить и проверить


# # Пример 3
# print('======= Пример 3 =======')
# # Проверка того, как усвоили
# d = 80
# while not d % 2:  # d % 2 == 0
#     print('старое значение d:', d)
#     d //= 2  # d = d // 2
#     print('новое значение d:', d)
# #
# print('Итоговое значение: ', d)  # Out: Вспомнить и проверить


# Бесконечный цикл
# while True:
#     print('hello, world!')  # Прервать Ctrl+C


# Пример 4
# Работа со строкой через цикл и индексы
# s = 'hello'
# index = 0
# while index < len(s):
#     print(s[index].upper(), end=' ')
#     index += 1
#
# print()
# print('Done')



# Пример 5
# Ключевое слово break в цикле
# i = 0
# s = 'hello python'
# # index изменяется в цикле от 0 до 11
# while i < len(s):
#     print(s[i].upper(), end=':')
#     if i == 6:
#         # прерывает цикл
#         break
#     i += 1
#
# print()
# print(f'{i = }')  #
# print('=' * 40)

# Пример 5.1
# i = 0
# s = "hello python"
# while i < len(s):
#     if s[i] == ' ':
#         # прерывает цикл
#         break
#     print(s[i], end='')
#     i += 1
#
# print()
# print('=' * 40)

# Пример 6
# Пример использования блока <else> в цикле while.

# string = input('Enter a string: ')
# char = input('Enter a character: ')
# while string:  # while len(string) > 0:
#     if string[0] == char:
#         print('FOUND')
#         break
#     # Присвоить значение с первого индекса по последний
#     string = string[1:]
#     print(string)
# # Этот блок отработает, если не было прерывания цикла(break)
# else:
#     print('Nothing')


# Проверка ввода 3x значного числа.
number = input("Enter a number (option:<устал>): ").lstrip('0')
while not number.isdigit() or len(number) != 3:
    if number == 'устал':
        break
    print('Bad input. Try again.')
    number = input("Enter a number: ").lstrip('0')
else:
    print(number, number[::-1])



