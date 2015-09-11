# coding=utf-8

from math import sqrt

__author__ = 'sford'


def multiples_of_3_and_5(num_count):
    # 1-я задача:
    # Находит сумму всех чисел меньше заданного числа, кратных 3 или 5.
    num_list = range(num_count)
    num_sum = sum([num for num in num_list if (num % 3 == 0) or (num % 5 == 0)])
    return num_sum


def sum_fibonacci_numbers(max_num):
    # 2-я задача:
    # Находит сумму всех четных элементов ряда Фибоначчи, которые не превышают заданного числа.
    fib_num_sum = 0
    fib_num = 0
    first_num = fib_num
    second_num = 1
    while fib_num <= max_num:
        fib_num = first_num + second_num
        first_num = second_num
        second_num = fib_num
        if not (fib_num % 2):
            fib_num_sum += fib_num
    return fib_num_sum


def max_prime_factor(num):
    # 3-я задача:
    # Находит самый большой делитель заданного числа, являющийся простым числом
    # Делитель не может быть больше квадратого корня заданного числа
    num_list = range(int(sqrt(num)), 1, -1)
    for i in num_list:
        if not (num % i):
            if is_prime_num(i):
                return i
    return 0


def is_prime_num(num):
    # Проверяет на простое число
    num_list = range(3, int(sqrt(num)), 2)
    for i in num_list:
        if not (num % i):
            return 0
    return num


def max_palindrome(num_size):
    # 4-я задача:
    # Находит самый большой палиндром, полученный умножением двух чисел заданного разряда.
    if num_size < 2:    # Проверка на разрядность для однозначных чисел
        return 0
    min_num = 10 ** (num_size - 1)  # Наименьшее значение полиндрома
    max_num = 10 ** num_size        # Наибольшее значение полиндрома
    palindrome = 0
    num_list = range(max_num, min_num, -1)
    for i in num_list:
        for j in num_list:
            product = i * j
            if product > palindrome:
                s_product = str(product)
                if s_product == s_product[::-1]:    # Проверка на полиндромность
                    palindrome = product
    return palindrome


def evenly_divisible_min_num(num_count):
    # 5-я задача:
    # Ищем самое маленькое число, которое делится без остатка на все числа заданного кол-ва
    num_list = range(num_count, int(num_count / 2), -1)    # Можно взять только пол диапазона
    prime_num_list = [x for x in num_list if is_prime_num(x)]  # Только простые числа
    min_num = reduce(lambda a, b: a * b, prime_num_list)    # Их произведение

    b_found = False
    while not b_found:          # Ищем то самое число
        for i in num_list:
            if min_num % i:
                min_num += 2    # Шаг тоже может быть кратен двум
                break
        else:
            b_found = True

    return min_num


def sum_square_difference(num_count):
    # 6-я задача:
    # Находит разность между суммой квадратов
    # и квадратом суммы певых натуральных чисел заданного кол-ва.
    num_list = range(num_count + 1)
    num_sum_square = sum([num for num in num_list])
    num_square_sum = sum([num*num for num in num_list])
    sum_square_diff = num_sum_square * num_sum_square - num_square_sum
    return sum_square_diff


def prime_num(num_idx):
    # 7-я задача:
    # Находит №-е простое число
    idx = 0
    for i in range(1, num_idx * num_idx, 2):
        if is_prime_num(i):
            idx += 1
            if idx == num_idx:
                num = i
                break
    return num


def max_series_product(s_product, num_count):
    # 8-я задача:
    # Находит наибольшее произведение определенного кол-ва последовательных цифр в заданном числе.
    i = 0
    i_max_product = 0
    zero_idx = s_product.find('0', i)
    while zero_idx > 0:
        dict_elem = s_product[i:zero_idx]
        if len(dict_elem) >= num_count:         # пропускаем элементы с кол-вом меньше заданного
            p_product = reduce(lambda a, b: int(a) * int(b), s_product[i:num_count])
            if p_product > i_max_product:       # если нашли элементы с бОльшим произведением
                i_max_product = p_product
            s_product = s_product[1:len(s_product)]
        else:
            s_product = s_product[zero_idx + 1:len(s_product)]
        while not s_product.find('0'):          # удаляем лидирующие нули
            s_product = s_product[1:len(s_product)]
        zero_idx = s_product.find('0', i)
    return i_max_product


def pythagorean_triplet(sum_num):
    # 8-я задача:
    # Находит произведение тройки Пифагора, для которой сумма равна заданному числу
    l_triplet = []
    uni_triplet = range(3, 6)    # 3, 4, 5
    uni_triplet_sum = sum(uni_triplet)
    if not (sum_num % uni_triplet_sum):     # проверка на однородность
        k = int(sum_num / uni_triplet_sum)
        l_triplet = [x * k for x in uni_triplet]
    else:
        pass
    triplet_product = reduce(lambda a, b: a * b, l_triplet)
    return triplet_product


