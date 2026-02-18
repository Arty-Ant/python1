
"""
Задача №3. Подсчет гласных в строке
Дана строка из латинских символов, нужно подсчитать кол-во
гласных в строке и вывести результат подсчета.

Гласные:
vowels = 'aeiou' или так
VOWELS = 'aeiou'

Подсказка. Используем цикл while, накопительную переменную
"""
VOWELS = 'aeiou'

string = input("Enter a string: ").lower()
counter = index = 0
while index < len(string):
    if string[index] in VOWELS:
        counter += 1
    index += 1


print(f"{counter = }")


