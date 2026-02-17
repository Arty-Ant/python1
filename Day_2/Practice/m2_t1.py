"""
Задача №1. Посчитать размер вклада на депозите за несколько лет.

Вход:
размер начального вклада (от 100 до 1_000_000 рублей)(float),
годовой процент начисления(от 1 до 20)(float) с ежегодной капитализацией,
количество лет по вкладу(от 1 до 100)(int).
Интервалы для чисел включительно

Выход:
Проверить введенные данные и посчитать итоговую сумму на счету для верных данных.
Если данные неверные, то вывести сообщение об этом.
! Циклы еще не придумали, а if уже придумали.
"""
# # Variant 1
deposit = float(input('Введите сумму вклада (100-1_000_000): '))
percent = float(input('Введите 1-20% годовых: '))
years = int(input('Введите количество лет (1-100): '))

if 100 <= deposit <= 1_000_000:
    if 1 <= percent <= 20:
        if 1 <= years <= 100:
            result = deposit * (1 + percent / 100) ** years
            print(f"Итоговая сумма будет {result:.2f} рублей")
        else:
            print("Количество лет должно быть от 1 до 100 лет")
    else:
        print("% должен быть от 1 до 20")
else:
    print("Вклад должен быть от 100 до 1 000 000")

# ==== Запрещенка =====
# Проверка того, что переменная существует в глобальной области видимости
if "result" in globals():
    print("Здесь есть result?", result)

# Variant 2
amount = float(input("Введите сумму вклада (от 100 до 1 000 000): "))
rate = float(input("Введите годовой процент (от 1 до 20): "))
years = int(input("Введите количество лет (от 1 до 100): "))

if amount < 100 or amount > 1_000_000:
    print("Ошибка: сумма вклада должна быть от 100 до 1 000 000 руб.")
elif rate < 1 or rate > 20:
    print("Ошибка: процентная ставка должна быть от 1 до 20%.")
elif years < 1 or years > 100:
    print("Ошибка: срок вклада должен быть от 1 до 100 лет.")
else:
    final_balance = amount * (1 + rate / 100) ** years
    profit = final_balance - amount

    print("-" * 40)
    print(f"Итоговая сумма через {years} лет: {final_balance:.2f} руб.")
    print(f"Чистая прибыль: {profit:.2f} руб.")

# Variant 3
init_money = float(input('Initial sum of money: '))
perc = float(input('Percentage per year: '))
years = int(input('Number of years: '))
if (100 <= init_money <= 1_000_000 and
        1 <= perc <= 20 and
        1 <= years <= 100):
    res = (init_money * (1 + perc / 100) ** years)
    print(f'In {years} years you will have {res:.2f} rub on your bank account.')
else:
    print('Data input error')
