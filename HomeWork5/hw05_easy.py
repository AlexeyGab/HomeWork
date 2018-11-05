import os

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

print("Задание 1:")

# Создадим директории 1-9
for i in range(1,10):
    name = f"dir_{i}"
    if not os.path.exists(name):
        os.mkdir(name)

# Удалим директории 1-9
for i in range(1,10):
    name = f"dir_{i}"
    if os.path.exists(name):
        os.rmdir(name)


# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

print("Задание 2:")

for val in os.listdir():
    if os.path.isdir(val):
        print(val)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys
import shutil

print("Задание 3:")
# Путь файла
file = sys.argv[0]
file = os.path.basename(file)
shutil.copy(file, file + "_copy")
