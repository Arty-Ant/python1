"""
Задача №2
Дана строка.
Необходимо посчитать количество вхождений каждого символа с помощью dict.

Пример:
In: Hello, Python1tt.
Out:
{'H': 1,
 'e': 1,
 'h': 1,
 'l': 2,
 'o': 2,
 ',': 1,
 'P': 1,
 'y': 1,
 't': 3,
 'n': 1,
 '1': 1,
 ' ': 1,
 '.': 1}
"""
import pprint

# Variant 1
s = input("enter a string: ")

counter = {}
for char in s:
    if char in counter:
        counter[char] += 1
    else:
        counter[char] = 1

pprint.pprint(counter, width=20, sort_dicts=False)

# Variant 2
s = input("enter a string: ")

counter = {}
for char in s:
    if char not in counter:
        counter[char] = s.count(char)

pprint.pprint(counter, width=20, sort_dicts=False)

# Variant 3
s = input("enter a string: ")

counter = {}
for char in set(s):
    counter[char] = s.count(char)

pprint.pprint(counter, width=20, sort_dicts=False)