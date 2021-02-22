"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""


def summary():
    try:
        with open('test_file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_digit = line.split()
            print(sum(map(int, my_digit)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набрано число.')
summary()