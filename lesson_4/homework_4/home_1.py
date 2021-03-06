"""Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах * ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
""" Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения необходимо запускать скрипт с параметрами."""


from sys import argv


def my_func_1():
    try:
        num = [int(_) for _ in argv[1:]]
        return (num[0] * num[1]) + num[2]
    except ValueError:
        return 'Вы ввели недопустимое значение'
    except IndexError:
        return 'Вы ввели недостаточное количество параметров'


print(my_func_1())
