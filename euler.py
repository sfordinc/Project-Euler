# coding=utf-8

from math import sqrt

__author__ = 'sford'


def multiples_of_3_and_5(num_count):
    # 1-я задача:
    # Находит сумму всех чисел меньше заданного числа, кратных 3 или 5.
    i = 1
    summ = 0
    while i < num_count:
        if (i % 3 == 0) or (i % 5 == 0):
            summ += i
        i += 1
    return summ


def sum_fibonacci_numbers(max_num):
    # 2-я задача:
    # Находит сумму всех четных элементов ряда Фибоначчи, которые не превышают заданного числа.
    summ = 0
    fib_num = 0
    fi = fib_num
    si = 1
    while fib_num <= max_num:
        fib_num = fi + si
        fi = si
        si = fib_num
        if not (fib_num % 2):
            summ += fib_num
    return summ


def max_prime_factor(num):
    # 3-я задача:
    # Находит самый большой делитель заданного числа, являющийся простым числом
    i = int(sqrt(num))  # Делитель не может быть больше квадратого корня заданного числа
    while i >= 1:
        if not (num % i):
            if is_prime_num(i):
                return i
        i -= 1
    return 0


def is_prime_num(num):
    # Проверяет на простое число
    i = 3
    sqrt_num = sqrt(num) + 1
    while i < sqrt_num:
        if not (num % i):
            return 0
        else:
            i += 2
    return num


def max_palindrome(num_size):
    # 4-я задача:
    # Находит самый большой палиндром, полученный умножением двух чисел заданного разряда.
    if num_size < 2:    # Проверка на разрядность для однозначных чисел
        return 0
    min_num = 10 ** (num_size - 1)  # Наименьшее значение полиндрома
    max_num = 10 ** num_size        # Наибольшее значение полиндрома
    palindrome = 0
    ra = range(max_num, min_num, -1)
    for i in ra:
        for j in ra:
            product = i * j
            if product > palindrome:
                s_product = str(product)
                if s_product == s_product[::-1]:    # Проверка на полиндромность
                    palindrome = product
    return palindrome


def evenly_divisible_min_num(num_count):
    # 5-я задача:
    # Ищем самое маленькое число, которое делится без остатка на все числа заданного кол-ва
    min_num = 2                                         # Число должно быть кратно двум
    i_num = range(num_count, int(num_count / 2), -1)    # И поэтому можно перебирать только пол диапазона
    for ii in i_num:                                    # Подсчитаем возможное минимальное число
        if is_prime_num(ii):
            min_num *= ii
    b_found = False
    while not b_found:                                  # Ищем то самое число
        for i in i_num:
            if min_num % i:
                min_num += 2                            # Шаг тоже может быть кратен двум
                break
        else:
            b_found = True
    return min_num


def sum_square_difference(num_count):
    # 6-я задача:
    # Находит разность между суммой квадратов
    # и квадратом суммы певых натуральных чисел заданного кол-ва.
    r_num = range(1, num_count + 1)
    num_square_sum = 0
    num_sum_square = 0
    for i_num in r_num:
        num_sum_square += i_num
        num_square_sum += i_num * i_num
    sum_square_diff = num_sum_square * num_sum_square - num_square_sum
    return sum_square_diff


def prime_num(num_idx):
    # 7-я задача:
    # Находит №-е простое число
    idx = 0
    for i in range(1, num_idx*num_idx, 2):
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
        if len(dict_elem) >= num_count:
            p_product = 1
            for ii in s_product[i:num_count]:
                p_product *= int(ii)
            if p_product > i_max_product:
                i_max_product = p_product
            s_product = s_product[1:len(s_product)]
        else:
            s_product = s_product[zero_idx + 1:len(s_product)]
        while not s_product.find('0'):  # удаляем лидирующие нули
            s_product = s_product[1:len(s_product)]
        zero_idx = s_product.find('0', i)
    return i_max_product
