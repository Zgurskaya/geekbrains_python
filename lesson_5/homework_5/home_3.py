"""
Создать текстовый файл (не программно). Построчно записать
фамилии сотрудников и величину их окладов (не менее 10 строк).
Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников.
Выполнить подсчёт средней величины дохода сотрудников.
Пример файла:
Иванов 23543.12
Петров 13749.32
"""


with open("test_file_3", "r") as my_file:
    sps = []
    small = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            small.append(i[0])
        sps.append(i[1])
print(f'Оклад меньше 20.000 у сотрудников {small}, средний оклад сосавдяет {sum(map(int, sps)) / len(sps)}')
