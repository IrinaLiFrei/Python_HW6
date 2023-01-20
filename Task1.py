# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

my_list = input('Enter several numbers separeted by spaces: ').split(' ')
my_list = list(map(int,(my_list)))
print(my_list)

# sum = 0                                                       # Старое решение
# for i in range (len(my_list2)):
#     if i % 2 != 0:
#         sum += my_list2[i]
# print(sum)

new_list = [i for i in my_list if i % 2 == 0]                   # List Compreh
# new_list = list(filter(lambda x: x%2 == 0, my_list))          # Filter
print(new_list)
sum = 0
for i in range (len(new_list)):
    sum += new_list[i]
print(sum)
