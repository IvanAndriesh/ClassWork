# Задание 1 
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a > b:
    print(a)
elif a < b:
    print(b)
else:
    print("Они равны")

# Задание 2
a = int(input("Введите первую сторону: "))
b = int(input("Введите вторую сторону: "))
c = int(input("Введите третью сторону: "))
if a + b >= c:
    print("Треугольник существует")
elif a + c >= b:
    print("Треугольник существует")
elif b + c >= a:
    print("Треугольник существует")
else:
    print("Треугольник не существует")

# Задание 3 
a = int(input("Введите год"))
if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
    print("Yes")
else:
    print("No")