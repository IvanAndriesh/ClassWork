# Задание 11
v = float(input("Введите объем: "))
m = float(input("Введите массу: "))
p = m * v
print("Плотность равна:", p)
# Задание 12
n1 = float(input("Введите первое число: "))
n2 = float(input("Введите второе число: "))
s = n1 + n2
p = n1 * n2
d = n1 / n2
v = n1 - n2
print("Сумма равна:", s,'\n' +
"Разность равна:", v, '\n' +
"Произведение равно:", p,'\n' +
"Частное равно:", d)
# Задание 13
n1 = float(input("Введите первое число: "))
n2 = float(input("Введите второе число: "))
sa = (n1 + n2)/2
sg = (n1 * n2)**0.5
print("Среднее арифмитическое равно:", sa, '\n' +
"Среднее геометрическое равно:", sg)
# Задание 14
l = int(input("Введите количество жителей: "))
p = float(input("Введите площадь государства: "))
pl = l / p
print("Плотность населения государства равно: ", pl)
# Задание 15
a1 = float(input("Введите первое ребро параллелепипеда: "))
a2 = float(input("Введите второе ребро параллелепипеда: "))
a3 = float(input("Введите третье ребро параллелепипеда: "))
v = a1 * a2 * a3
pl = 2 * (a1*a2 + a1*a3 + a2*a3)
print("Площадь поверхности равна:", pl,'\n' +
"Объём равен:", v)