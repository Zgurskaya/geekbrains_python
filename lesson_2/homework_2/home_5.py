# Реализовать структуру "Рейтинг"
my_list = [7, 7, 5, 4, 4, 2, 1]
print(f"список - {my_list}")
число = int(input("Введите натуральное число: "))
for i in range(0, len(my_list)):
    if my_list[i] == число:
        my_list[i+1] < число
        my_list.insert(i+1, число)
        break
    elif my_list[0] < число:
         my_list.insert(0, число)
    elif my_list[-1] > число:
        my_list.append(число)
print(my_list)
