# coding: UTF-8

__author__ = 'Габеркорн Алексей Игоревич'

import random
import math

# Задача-1: Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

# Получим целое положительное число от генератора случаных чисел
value = random.randrange(0,100000)
print('Случайное число:', value)

# найдем максимальную цифру с помощью цикла for
maximum = 0
for s in str(value):
    digit = int(s)
    if maximum < digit:
        maximum = digit

print('Максимальная цифра:', maximum)

# найдем максимальную цифру с помощью цикла while
maximum = 0
while(value != 0):
    digit = value % 10
    if maximum < digit:
        maximum = digit
    value = value // 10

print('Максимальная цифра:', maximum)

# Задача-2: Исходные значения двух переменных запросить у пользователя.
# Поменять значения переменных местами. Вывести новые значения на экран.
# Решите задачу, используя только две переменные.
# Подсказки:
# * постарайтесь сделать решение через действия над числами;
# * при желании и понимании воспользуйтесь синтаксисом кортежей Python.

#Решение через XOR (только для целых чисел)
a = int(input('Введите целое число a:'))
b = int(input('Введите целое число b:'))

a ^= b
b ^= a
a ^= b

print('Переменная a =', a)
print('Переменная b =', b)

#нашел еще простой обмен двух переменных
#a, b = b, a
# про синтаксисом кортежей не знаю

# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

print('Решаем квадратное уравнение!')
a = float(input('Введите коэфициент а:'))
b = float(input('Введите коэфициент b:'))
c = float(input('Введите коэфициент c:'))

# Найдем дискриминант
D = b**2 - 4 * a * c
# Если D > 0 - имеем два корня x1, x2
# Если D == 0 - имеем один корень x
# Если D < 0 - корней нет

if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print('Найдены два корня, x1 =', x1, 'x2 =', x2)
elif D == 0:
    x = (-b) / (2 * a)
    print('Найден один корень, x =', x)
else:
    print('Корней нет!')