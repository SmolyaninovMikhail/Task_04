# Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств. (может быть с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.

def up_sort(some_set):
    for _ in range(len(some_set)):
        print(min(some_set), end=' ')
        some_set.remove(min(some_set))

import random
set_a = {random.randint(-10, 11) for _ in range(int(input('n = ')))}
print(set_a)
set_b = {random.randint(-10, 11) for _ in range(int(input('m = ')))}
print(set_b)
set_c = set_a & set_b
print(set_c)
up_sort(set_c)