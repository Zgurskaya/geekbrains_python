"""
Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать
параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.
"""


def viz_func(**kwargs):
    return list(kwargs.items())


print(viz_func(name="Геннадий", family="Северный", year="1995", city="Астрахань", email="gnoth@gmail.ru",
               tel="89940901108"))
