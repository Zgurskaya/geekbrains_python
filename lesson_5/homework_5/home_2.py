"""
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
"""


my_file = open("test_file_2")
line_number_end = 0
for line_number, line in enumerate(my_file):
    print(f"Текст строки: \n {line}", end="")
    print(f"Количество слов в {[line_number]} строке: {len(line.split())}")
    line_number_end = line_number
    print("Количество строк", line_number_end + 1)
my_file.close()
