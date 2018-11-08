# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import shutil

def goToDir(path):
    os.chdir(path)
    pass

def showDir(path = ''):
    if path == '':
        print(os.listdir())
    else:
        print(os.listdir(path))
    pass

def delDir(path):
    shutil.rmtree(path)
    pass

def createDir(path):
    os.mkdir(path)
    pass


commands = {
    1: goToDir,
    2: showDir,
    3: delDir,
    4: createDir
}

def printMenu():
    print("Что нужно сделать?")
    print("1 - перейти в указанную папку")
    print("2 - показать содержимое папки")
    print("3 - удалить папку")
    print("4 - создать папку")

while(True):
    printMenu()
    command = int(input("Код операции:"))
    path = input("Имя папки:")
    commands[command](path)
