# 6.
# Дан массив целых чисел,
# отсортируйте массив в порядке
# возрастания в зависимости от
# частоты значений.
#
# Вернуть отсортированный массив.

# arr = [5, 1, 8, 2, 4, 6]
# temp = 0
# print("Элементы исходного массива: ")
# for i in range(0, len(arr)): print(arr[i], end=" ")
# # sort: 2 Вариант if(arr[i] < arr[j]):
# for i in range(0, len(arr)):
#     for j in range(i+1, len(arr)):
#         if(arr[i] > arr[j]):
#             temp = arr[i]
#             arr[i] = arr[j]
#             arr[j] = temp
# print()
#
# print("Элементы массива отсортированы: ")
# for i in range(0, len(arr)):
#     print(arr[i], end=" ")


# 7.

# Вам дан массив nums, состоящий
# из целых положительных чисел.
#
# Вы должны взять каждое целое число
# в массиве, поменять местами его цифры
# и добавить новое число в конец массива.
#
# По итогу надо вернуть количество уникальных
# целых чисел в конечном массиве.

from random import randint

mass = int(input('Введите количество элементов: '))
a, b = map(int, input('Введите диапозон ОТ - ДО: ').split())
A = [randint(a, b) for x in range(mass)]
print('Масcив:', A)
for i in range(0, mass-1, 2):
    A[i], A[i+1] = A[i+1], A[i]
print('Масcив с перестaновкой элементов:', A)
# 8.

# Дан массив целых чисел nums.
# Верните максимальное значение такое, что:
# (nums[i]-1)*(nums[j]-1).
# Я уехал в комондировку, сколько смог столько и сделал до вторника надеюсь приеду
