amount = 0
tickets = (int(input("Сколько билетов будете бронировать?:")))
ages = (int(input("Введите возраст посетителя")) for age in range (tickets))
for age in ages:
    if age < 18:
        amount += 0
    elif age >= 18 and age <= 25:
        amount += 990
    elif age > 25:
        amount += 1390
        if tickets > 3:
            amount -= amount / 100 * 10
        print("Стоимость ваших билетов", amount)

