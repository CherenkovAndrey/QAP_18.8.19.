print("")
tickets = 0
while tickets < 1:
    tickets = int(input("Укажите необходимое количество билетов: "))
    if tickets > 0: break
    print("Недопустимое количество билетов!")

print("")
price = 0
visitors = 0
while visitors != tickets:
    visitors += 1
    age = -1
    while age < 0:
        age = int(input("Укажите возраст поситителя № " + str(visitors) + ": "))
        if 0 <= age < 18:
            price += 0
        elif 18 <= age < 25:
            price += 990
        elif 25 <= age:
            price += 1390
        else:
            print("Возраст не может быть отрицательным!")

print("")
if tickets > 3:
    print("Итоговая сумма: ", int(price * 0.9), "рублей. С учётом скидки 10%.")
else:
    print("Итоговая сумма: ", int(price), "рублей.")
