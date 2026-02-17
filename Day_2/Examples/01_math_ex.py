# Добавление математического модуля
import math


# Множественное присваивание
# Важно: кол-во переменных равно кол-во значений
a, b, e, f = 5, 2, 'hello', True
c = d = k = m = 0


# # Математические операции
# print('a + b =', a + b)
# print('a - b =', a - b)
# print('a * b =', a * b)
# print('a / b =', a / b)    # Тип результа всегда float!
# print('a // b =', a // b)  # Целочисленное деление -> out: 2
# print('a % b =', a % b)    # Остаток от деления -> out: 1
# print('a ** b =', a ** b)  # Возведение в степень -> out: 25
#
# # операция возведения в степень правоассоциативна!
# print('(a ** b) ** 0.5 =', (a ** b) ** 0.5)  # Извлечение квадрата
#
# # Тот же самый результат
# message = 'Извлечение квадрата с помощью модуля math:'
# print(message, math.sqrt(a)) # 5 ** 0.5

# Не забываем про функцию help()
# help(math.sqrt)
# print(type(math))
# help(math)

# Синтаксический сахар (Syntax sugar)
# a = a + 1
# print('a =', a)
#
# # a = a + 1
# a += 1
# print('a += 1:', a)
# #
# # a = a - 2
# a -= 2
# print('a -= 2:', a)
#
# # a = a * 3
# a *= 3
# print('a *= 3:', a)
#
# # b = b / 4  # b = 2
# b /= 4
# print('b /= 4:', b)
#
# # a = a // 3
# a //= 3
# print('a //= 3:', a)
#
# # a = a % 2
# a %= 2
# print('a %= 2:', a)
#
# # Длинная арифметика
# c = 7
# c **= 3000
# print(type(c))

# Сравниваем число с +бесконечностью
# print(c > float('inf'))

# Плюс бесконечность. Самое большое число
# print(float('inf'))

# Минус бесконечность. Самое маленькое число
# print(float('-inf'))

# Важный момент хранение дробных чисел в памяти компьютера
# a = 0.1 * 3.0
# print(a == 0.3)  #
# print(type(a), a)

# Округление до 15-ми разрядов после запятой
# print(round(0.1 * 3, 15) == 0.3)

# Округление до сотен
# print(round(1244.5678, -2))  # Out -> 1200.0


# https://stackoverflow.com/questions/33019698/how-to-properly-round-up-half-float-numbers
# https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
# https://en.wikipedia.org/wiki/Rounding#Round_half_to_even
