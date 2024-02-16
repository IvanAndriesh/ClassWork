# ЗАДАНИЕ 1 
a = int(input("Введите значение: "))
if a > 0: 
    print("Число больше 0")
elif a < 0:
    print("Число меньше 0")
else:
    print("Число равно 0")
# ЗАДАНИЕ 2
a = int(input("Введите значение: "))
if a > 0: 
    print(1)
else:
    print(-1)
# ЗАДАНИЕ 3
zadiak = ["Козерог", "Водолей", "Рыбы", "Овен", "Телец", "Близнецы", "Рак", "Лев", "Дева", "Весы", "Скорпион", "Стрелец"]
while True:
    mounth_numb = int(input("Введите месяц: "))
    if mounth_numb >= 1 and mounth_numb <= 12:
        print("Ваш знак зодиака", zadiak[mounth_numb - 1])
    else:
        print("Вы ввели нерпавильный месяц")
        break
# Задание 4 
a = int(input("введите 1 число: "))
b = int(input("введите 2 число: "))
c = 0
if a > b:
    c += a - b 
    print("ответ: ", c)
elif a < b: 
    c += a + b 
    print("ответ: ", c)
else: 
    c += a 
    print("ответ: ", c)
# Задание 5 
a = int(input("введите значение 1 числа: "))
b = int(input("введите значение 2 числа: "))
c = int(input("введите значение 3 числа: "))
if a > b + c:
    a += b + c 
    print("Ответ: ", a)
elif a < b + c: 
    a += b - c 
    print("Ответ: ", a)
elif  с == 0 and a > b: 
    a += b 
    print("Ответ: ", a)
elif  b == 0 and a > c: 
    a += c
    print("Ответ: ", a)
else: 
    print("Значения равны")