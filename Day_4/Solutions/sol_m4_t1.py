import random as rnd

# Фиксация random'a
# rnd.seed(0)

numbers = []
for _ in range(20):
    numbers.append(rnd.randint(1, 4))

print(f'{numbers = }')

# Удалить все 3(тройки) из списка
# На выходе нужен список без троек

# Variant 1
nums1 = numbers.copy()
NUMBER = 3
while NUMBER in nums1:
    nums1.remove(NUMBER)

print(f'{nums1 = }')

# Variant 2
nums2 = numbers.copy()
counts = nums2.count(NUMBER)
for _ in range(counts):
    nums2.remove(NUMBER)

print(f'{nums2 = }')

# Variant 3
without_three = []
for number in numbers:
    if number != NUMBER:
        without_three.append(number)

print(f'{without_three = }')

# Variant 4, плохой вариант.
# Сильно не рекомендуется менять список во время прохождения(итерации) по нему
nums4 = numbers[:]
for number in nums4:
    if number == NUMBER:
        nums4.remove(number)

print(f'{nums4 = }')

# Variant 5
nums5 = [3, 3, 1, 2, 3, 3, 4, 1]
for number in nums5[:]:
    if number == NUMBER:
        nums5.remove(number)

print(f'{nums5 = }')

# Variant 6
numbers = [3, 3, 1, 2, 3, 3, 4, 1]
i = 0
while i < len(numbers):
    if numbers[i] == 3:
        numbers.pop(i)
    else:
        i += 1

print(f'{numbers = }')
