# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между
# максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

my_list = input('Enter several numbers separeted by spaces: ').split(' ')
my_list = list(map(float,(my_list)))
# new_list = []                                             # Старое решение
# for i in my_list:
#     new_list.append(round(i - int(i), 3))
new_list = [round(i - int(i), 3) for i in my_list]          # Новое решение
print(new_list)

while 0.0 in new_list:
    new_list.remove(0.0) 

res = max(new_list) - min(new_list)
print(res)

