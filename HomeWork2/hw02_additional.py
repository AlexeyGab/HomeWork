
# coding: UTF-8

__author__ = 'Габеркорн Алексей Игоревич'

import random

# Доп. дз

# 1) Написать программу, которая генерирует список со случайными значениями. (модуль random в помощь)

print("Задание 1:")

m = []
# Заполним список случайными значениями
for i in range(5):
    m.append(random.randrange(0, 10))

print(m)

# 2) Найдите сумму чисел списка, которые стоят на четных местах.
print("Задание 2:")
sum = 0
for val in m[1::2]:
    sum += val

print("Сумма чисел, стоящих на четных местах=", sum)

# 3) Сделать универсальное решение для того, чтобы можно было отсортировать словарь по значениям
    # не понял задание =( словарь может только числа, только строки?
    #  или вобще все что угодно? числа, строки, кортежи, другие словари все в кучу?

# 4) Сформировать пять списков разной длины и найти в них элементы, которые есть в каждом списке
print("Задание 4:")

m1 = [1, 2, 3, 4, 5, 6]
m2 = [5, 6, 7, 8, 9, 10, 11]
m3 = [6, 14]
m4 = [5, 6, 1]
m5 = [5, 6, 11, 3, 8]

mset = set(m1).intersection(m2).intersection(m3).intersection(m4).intersection(m5)

print(mset)