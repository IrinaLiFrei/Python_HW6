# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, 
# второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

my_list = input('Enter several numbers separeted by spaces: ').split(' ')
my_list2 = list(map(int,(my_list)))
print(my_list2)

if len(my_list2)%2 == 0:
    half_length = int(len(my_list2)/2)
    new_list1 = my_list2[:half_length]
    new_list2 = my_list2[half_length:]
    new_list2.reverse()
    
else:
    half_length = int(len(my_list2)//2 + 1)
    new_list1 = my_list2[:half_length]
    new_list2 = my_list2[half_length-1:]
    new_list2.reverse()

# new_list3 = []                                                 # Старое решение
# for i in range(half_length):
#     new_list3.append(new_list1[i] * new_list2[i])
# print(new_list3)

new_list3 = [new_list1[i] * new_list2[i] for i in range(half_length)]            # List Compreh                                       # 
print(new_list3)


