# 1 Задача

floor = int(input("Enter the number of your foor: "))
room = int(input("Enter the number of your room: "))
print(f"You are living at {floor} flour in {room} room")

# 2 Задача

time = int(input("Введите время в секундах: "))
time_min = int((time%3600)/60)
time_h = int(time/3600)
time_sec = int(time-(time_h*3600 + time_min*60))
print(f"Ваше время {time_h:02}:{time_min:02}:{time_sec:02}")

# 3 Задача

n = input("Введите любое число: ")
print(f"{n}+{n+n}+{n+n+n} = {int(n)+int(n+n)+int(n+n+n)}")

# 4 Задача ( честно, подсмотрел на разборе, но разобрался)

num1 = int(input("ведите число: "))
big_n = 0
n = num1
while n > 0:
    digit = n % 10
    if digit > big_n:
        big_n = digit
    n = n // 10
print(f"{big_n}")

# 5 Задача

revenue = int(input("Введите значение выручки компании за месяц: "))
costs = int(input("Введите значение издержок компании за месяц: "))
if revenue > costs:
    print("Ваша компания прибыльная в этом месяце")
else:
    print("Ваша компания убыточная в этом месяце")

# 6 Задача

revenue = int(input("Введите значение выручки компании за месяц: "))
costs = int(input("Введите значение издержок компании за месяц: "))
if revenue > costs:
    print("Ваша компания прибыльная в этом месяце")
    profit = revenue - costs
    rent = profit / revenue * 100
    office = int(input("Введите количество сотрудников компании: "))
    zrp = profit / office
    print(f"Рентабельность вашей компании состоавила {rent}, прибыль фирмы в расчеты на одного сотрудника {zrp}")
else:
    print("Ваша компания убыточная в этом месяце")

# 7 Задача

a = int(input("Введите количество километров, преодоленное за первый день пробежки: "))
b = int(input("Желаемый результат: "))
day = 1
while a < b:
    a = a * 1.1
    day = day + 1
print(f"на {day} день пробежки спортстмен достигнет результата {b} километров")





