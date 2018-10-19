# coding: UTF-8

__author__ = 'Габеркорн Алексей Игоревич'

# Задание-1: уравнение прямой вида y = kx + b задано в виде строки.
# Определить координату y точки с заданной координатой x.

equation = 'y = -12x + 11111140.2121'
x = 2.5
# вычислите и выведите y
print("Задание 1:")
# Уберем все пробелы из строки
equation = equation.replace(" ", "")

# Найдем значение коэфициента k
k = equation[equation.find("=") + 1 : equation.find("x")]
k = float(k)
# Найдем значение коэфициента b
b = equation[equation.find("x") + 1 :]
b = float(b)
print("k=", k)
print("b=", b)

# Вычислим y
y = k * x + b

print("y=", y)

# Задание-2: Дата задана в виде строки формата 'dd.mm.yyyy'.
# Проверить, корректно ли введена дата.
# Условия корректности:
# 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
#  (в зависимости от месяца, февраль не учитываем)
# 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
# 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
# 4. Длина исходной строки для частей должна быть в соответствии с форматом 
#  (т.е. 2 символа для дня, 2 - для месяца, 4 - для года)

# Пример корректной даты
date = '01.11.1985'

# Примеры некорректных дат
date = '01.22.1001'
date = '1.12.1001'
date = '-2.10.3001'

print("Задание 2:")
# Разберем строку первым выполним требование #4
# Для начала у нас в строке должно быть минимум две точки.
oneDotPos = 0
twoDotPos = 0
oneDotPos = date.find('.')
if(oneDotPos != -1):
    twoDotPos = date[oneDotPos+1:].find('.')
    twoDotPos += oneDotPos + 1

# так же наша строка должна содержать только цифры
digits = "1234567890"

# Если позиция второй точки не равна -1 значит две точки есть
if(twoDotPos != -1):
    day = date[:oneDotPos]
    month = date[oneDotPos+1 : twoDotPos]
    year = date[twoDotPos+1:]

    # Проверим длину дня, месяца, года
    lenghtOK = False
    if len(day) == 2 and len(month) == 2 and len(year) == 4:
        lenghtOK = True
    else:
        print("Неверный формат даты. Неправильные длины подстрок")

    # проверим что все символы это числа
    digitDayOK = False
    digitMonthOK = False
    digitYearOK = False
    if(lenghtOK):
        if day[0] in digits and day[1] in digits:
            digitDayOK = True
        if month[0] in digits and month[1] in digits:
            digitMonthOK = True
        if year[0] in digits and year[1] in digits and year[2] in digits and year[3] in digits:
            digitYearOK = True

    #Когда убедились что у нас только цифры
    if digitDayOK and digitMonthOK and digitYearOK:
        day = int(day)
        month = int(month)
        year = int(year)

        # 3. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999
        if 1 <= year <= 9999:
            # 2. Месяц должен приводиться к целому числу в диапазоне от 1 до 12
            if 1 <= month <= 12:
                # 1. День должен приводиться к целому числу в диапазоне от 1 до 30(31)
                #  узнаем сколько дней должно быть в месяце
                #  https://habr.com/post/261773/
                dayPerMonth = 30 + (month + (month//8)) % 2
                if 1 <= day <= dayPerMonth:
                    print("Дата введена корректно!")
                else:
                    print("Неверный формат даты. День должен приводиться к целому числу в диапазоне от 1 до 30(31)")
            else:
                print("Месяц должен приводиться к целому числу в диапазоне от 1 до 12")
        else:
            print("Неверный формат даты. Год должен приводиться к целому положительному числу в диапазоне от 1 до 9999")
    else:
        print("Неверный формат даты. В строке содержатся лишние символы")
else:
    print("Неверный формат даты. Нет точек")


# Задание-3: "Перевёрнутая башня" (Задача олимпиадного уровня)
#
# Вавилонцы решили построить удивительную башню —
# расширяющуюся к верху и содержащую бесконечное число этажей и комнат.
# Она устроена следующим образом — на первом этаже одна комната,
# затем идет два этажа, на каждом из которых по две комнаты, 
# затем идёт три этажа, на каждом из которых по три комнаты и так далее:
#         ...
#     12  13  14
#     9   10  11
#     6   7   8
#       4   5
#       2   3
#         1
#
# Эту башню решили оборудовать лифтом --- и вот задача:
# нужно научиться по номеру комнаты определять,
# на каком этаже она находится и какая она по счету слева на этом этаже.
#
# Входные данные: В первой строчке задан номер комнаты N, 1 ≤ N ≤ 2 000 000 000.
#
# Выходные данные:  Два целых числа — номер этажа и порядковый номер слева на этаже.
#
# Пример:
# Вход: 13
# Выход: 6 2
#
# Вход: 11
# Выход: 5 3