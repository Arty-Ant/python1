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

# === Ваш код ===

# Variant 1
num=int(input("Введите любое натуральное число: "))
result=digit=0
text=""
while num>0:
    digit=num%10
    result+=digit
    num//=10
    text+=f"{digit}"
    if num != 0:
        text+=" + "
print(f"{text[::-1]} = {result}")

# Variant 2
# num=input("Введите любое натуральное число: ")
# result=i=0
# text=""
# for i in range (len(num)):
#     text+=f"{num[i]}"
#     result+=int(num[i])
#     i+=1
#     if i != len(num):
#         text+=" + "
# print(f"{text} = {result}")

