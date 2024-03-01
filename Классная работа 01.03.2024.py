import math
# Задание 1
class Tourist:
    def __init__(self, last_name, country, year, cost):
        self.last_name = last_name
        self.country = country
        self.year = year
        self.cost = cost

    def display_info(self):
        print(f"Фамилия: {self.last_name}")
        print(f"Страна тура: {self.country}")
        print(f"Год поездки: {self.year}")
        print(f"Стоимость тура: {self.cost}")

tourist1 = Tourist("Иванов", "Италия", 2021, 1500)

print("Информация о туристе:")
tourist1.display_info()

last_name = input("\nВведите фамилию туриста: ")
country = input("Введите страну тура: ")
year = int(input("Введите год поездки: "))
cost = float(input("Введите стоимость тура: "))

tourist1.last_name = last_name
tourist1.country = country
tourist1.year = year
tourist1.cost = cost

print("\nОбновленная информация о туристе:")
tourist1.display_info()

# Задание 2

A = int(input("\nВведите значение А: "))
B = int(input("\nВведите значение B: "))
C = int(input("\nВведите значение C: "))

result = A*(B/3.14)+(C*3+5)
print("\n", result)

#Задание 3
R, Y = map(float, input("Введите значения R и Y через пробел: ").split())
result = R * Y**2 + (Y / 5)
print(f"Результат выражения R*{Y}**2+(Y/5) равен {result}")

#Задание 4
E = float(input("Введите вещественное положительное число: "))
print(f"Целая часть {int(E)}, дробная часть {E - int(E)}, корень {math.sqrt(E)}, остаток деления на 5 {E%5}")

#Задание 5
minutes = int(input("Введите количество минут, прошедших с 0 часов: "))

hours = minutes // 60
minutes_remainder = minutes % 60

print(f"Прошло {hours} часов и {minutes_remainder} минут")

#Задание 6
c = [213,421,432,532,124,13,42,435,46,232]
d = []
for i in range(len(c)):
    d.append(c[i] * c[i] - 5)
print(f' {c} \n {d}')
for i in range(len(c)):
    print(f"[{c[i]}]")
for i in range(len(c)):
    print(f"[{d[i]}]")  

#Задание 7
planets = [0] * 9

for i in range(len(planets)):
    planets[i] = float(input(f"Введите радиус {i+1}-й планеты: "))

max_planet = 0
min_planet = 0

for i in range(len(planets)):
    if planets[i] > planets[max_planet]:
        max_planet = i
    if planets[i] < planets[min_planet]:
        min_planet = i

print(f"Самая большая планета: {max_planet + 1}")
print(f"Самая маленькая планета: {min_planet + 1}")

#Задание 8 
numb = [0] * 12

for i in range(len(numb)):
    numb[i] = float(input(f"Введите {i+1}-й элемент: "))
for i in range(len(numb)):
    if numb[i] == 0:
        print(f"Нулевое значение у {i+1} элемента")