"""
Задача №1.
Вводим любое натуральное число.
Нужно посчитать сумму цифр числа, с помощью цикла while и for

# Variant 1 (while, с помощью математики, число - это int)
# Variant 2 (for, используем число как строку)

Пример:
In: 4521
Out: 12  

*Дополнительное задание:
4 + 5 + 2 + 1 = 12 - добавить к выводу сумму как выражение
"""
# Variant 1
num = int(input("Введите любое натуральное число: "))
result = digit = 0
text = ""
while num:
    digit = num % 10
    result += digit
    num //= 10
    text = f"{digit} + {text}"

print(f"{text[:-3]} = {result}")

# Variant 2
number = input("Введите любое натуральное число: ")
result = 0
text = ""
for digit in number:
    text += f"{' + ' * bool(text)}{digit}"
    result += int(digit)

print(f"{text} = {result}")
