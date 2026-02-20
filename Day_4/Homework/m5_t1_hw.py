"""
Задача №1

Написать программу, которая расшифрует строку,
используя набор букв из модуля string(string.ascii_lowercase),
Каждый символ - это две цифры.
Отчет с '00' -> 'a', '01' -> 'b' и до '25' -> 'z',
'26' - это пробел, он не входит в набор букв, нужно будет добавить
Вход: строка из цифр. Выход: Текст.

Рекомендация. Используем словари.

Проверка работы программы выполняется через другую строку, т.е.
переменная code - это один из тестовых вариантов.

Примеры строк:
'why not'
'how are you'

Дополнительное задание:
* добавить код и для зашифровки


"""
import string as st, pprint

code = '070411111426152419071413'
dic={}
i=0
for char in st.ascii_lowercase:
    dic[f'{i:0>2}']=char
    i+=1
dic["26"]=" "
char1=0
char2=2
result=""
for dig in code[::2]:
    num=code[char1:char2]
    result+=dic.get(num)
    char1+=2
    char2+=2
print(result)

# word = "how are you"
# val_list=[]
# i=0
# for char in st.ascii_lowercase:
#     val_list.append([char, f'{i:0>2}'])
#     i+=1
# val_list.append([" ", "26"])
# for char in word:
    
# print(val_list)


