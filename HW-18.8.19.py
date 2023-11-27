tickets = None
while tickets is None or tickets <= 0:
    try:
        tickets = int(input('Введите количество билетов: '))
        if tickets <= 0:
            raise Exception()
    except:
        print('Количество билетов должно быть целым положительным числом.')
total = 0
#ages = []
for i in range(tickets):
    age = None
    while age is None or not(0 <= age <= 100):
        try:
            age = int(input(f'Введите полное количество лет {i + 1}-го посетителя: '))
            if not(0 <= age <= 100):
                raise Exception()
        except:
            print('Возраст должен быть целым числом от 0 до 100.')
        else:
            #ages.append(age)
            if 18 <= age <= 25:
                total += 990
            elif 25 < age:
                total += 1390
if tickets > 3:
    total *= 0.9
#print(ages)
print(f'Сумма к оплате: {int(total)} рублей.')