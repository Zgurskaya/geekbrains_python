"""
Создать программный файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных будет свидетельствовать пустая строка.
"""

file = open("test_file", "w")
# Откроем ткстовый файл для записи"
line = input("Введите текст \n")
while line:
    file.writelines(line)
    line = input("Введите текст \n")
    if not line:
        break
file.close()


file = open("test_file", "r")
content = file.readline()
print(content)
file.close()

