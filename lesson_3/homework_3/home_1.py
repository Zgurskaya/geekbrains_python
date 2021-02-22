# Деление чисел
# Функция принимает два числа
# Если делитель равен нулю - деление невозможно
# Функция делит число var_1 на число var_2


def my_division_func():
    val_1 = float(input("Введите число val_1= "))
    val_2 = float(input("Введите число val_2= "))
    if val_2 == 0:
        pass
    else:
        return val_1 / val_2


print(my_division_func())
