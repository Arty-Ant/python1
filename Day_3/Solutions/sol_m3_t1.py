"""
Задание для практики:
Как вывести алфавит с помощью модуля string:
Aa Bb Cc Dd ... Zz?

string.ascii_lowercase  # 'abcdefghijklmnopqrstuvwxyz'
string.ascii_uppercase  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
"""


# Задаю другое имя(алиас) для модуля string,
# чтобы просто короче к нему обращаться
import string as st

lower = st.ascii_lowercase
upper = st.ascii_uppercase

# Variant 1
index = 0
while index < len(lower):
    print(f'{upper[index]}{lower[index]}', end=' ')
    index += 1

print()
# Variant 2
out = '' # накопительная переменная
index = 0
while index < len(lower):
    out += f'{lower[index].upper()}{lower[index]} '
    index += 1

print(out)
