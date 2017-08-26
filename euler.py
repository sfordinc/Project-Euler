# coding=utf-8
"""
набор задач по проекту "Эйлер"
"""
from math import sqrt

__author__ = 'sford'


def multiples_of_3_and_5(num_count):
    """
    1-я задача:
    Находит сумму всех чисел меньше заданного числа, кратных 3 или 5.

    :param num_count:
    :return: num_sum:
    """
    num_list = range(num_count)
    num_sum = sum([num for num in num_list if (num % 3 == 0) or (num % 5 == 0)])
    return num_sum


def sum_fibonacci_numbers(max_num):
    """
    2-я задача:
    Находит сумму всех четных элементов ряда Фибоначчи, которые не превышают заданного числа.

    :param max_num:
    :return: fib_num_sum:
    """
    fib_num_sum = 0
    fib_num = 0
    first_num = fib_num
    second_num = 1
    while fib_num <= max_num:
        fib_num = first_num + second_num
        first_num = second_num
        second_num = fib_num
        if fib_num % 2 == 0:
            fib_num_sum += fib_num
    return fib_num_sum


def max_prime_factor(num):
    """
    3-я задача:
    Находит самый большой делитель заданного числа, являющийся простым числом.
    Делитель не может быть больше квадратого корня заданного числа.

    :param num:
    :return: prime_factor
    """
    prime_factor = 0
    num_list = range(int(sqrt(num)), 1, -1)
    for i in num_list:
        if num % i == 0:
            if is_prime_num(i):
                prime_factor = i
                break
    return prime_factor


def is_prime_num(num):
    """
    Проверяет на простое число (>16 и нечетное)

    :param num:
    :return: num: ноль, если непростое число.
    """
    num_list = range(3, int(sqrt(num)) + 1, 2)
    for i in num_list:
        if num % i == 0:
            num = 0
            break
    return num


def max_palindrome(num_size):
    """
    4-я задача:
    Находит самый большой палиндром, полученный умножением двух чисел заданного разряда.
    Проверка на разрядность для однозначных чисел.

    :param num_size:
    :return: palindrome:
    """
    if num_size < 2:
        return 0
    # Наименьшее значение полиндрома
    min_num = 10 ** (num_size - 1)
    # Наибольшее значение полиндрома
    max_num = 10 ** num_size
    palindrome = 0
    num_list = range(max_num, min_num, -1)
    for i in num_list:
        for j in num_list:
            product = i * j
            if product > palindrome:
                s_product = str(product)
                # Проверка на полиндромность
                if s_product == s_product[::-1]:
                    palindrome = product
    return palindrome


def evenly_divisible_min_num(num_count):
    """
    5-я задача:
    Ищем самое маленькое число, которое делится без остатка на все числа заданного кол-ва.
    Можно взять только пол диапазона.

    :param num_count:
    :return: min_num:
    """
    num_list = range(num_count, int(num_count / 2), -1)
    # Только простые числа
    prime_num_list = [x for x in num_list if is_prime_num(x)]
    # Их произведение
    min_num = reduce(lambda a, b: a * b, prime_num_list)

    b_found = False
    # Ищем то самое число
    while not b_found:
        for i in num_list:
            if min_num % i:
                # Шаг тоже может быть кратен двум
                min_num += 2
                break
        else:
            b_found = True

    return min_num


def sum_square_difference(num_count):
    """
    6-я задача:
    Находит разность между суммой квадратов
    и квадратом суммы певых натуральных чисел заданного кол-ва.

    :param num_count:
    :return: sum_square_diff:
    """

    num_list = range(num_count + 1)
    num_sum_square = sum([num for num in num_list])
    num_square_sum = sum([num ** 2 for num in num_list])
    sum_square_diff = num_sum_square ** 2 - num_square_sum
    return sum_square_diff


def prime_num(num_idx):
    """
    7-я задача:
    Находит №-е простое число

    :param num_idx:
    :return: result:
    """
    result = 0
    idx = 0
    for i in range(1, num_idx * num_idx, 2):
        if is_prime_num(i):
            idx += 1
            if idx == num_idx:
                result = i
                break
    return result


def max_series_product(s_product, num_count):
    """
    8-я задача:
    Находит наибольшее произведение определенного кол-ва последовательных цифр в заданном числе.

    :param s_product:
    :param num_count:
    :return: i_max_product:
    """
    i = 0
    i_max_product = 0
    zero_idx = s_product.find('0', i)
    while zero_idx > 0:
        dict_elem = s_product[i:zero_idx]
        # пропускаем элементы с кол-вом меньше заданного
        if len(dict_elem) >= num_count:
            p_product = reduce(lambda a, b: int(a) * int(b), s_product[i:num_count])
            # если нашли элементы с бОльшим произведением
            if p_product > i_max_product:
                i_max_product = p_product
            s_product = s_product[1:len(s_product)]
        else:
            s_product = s_product[zero_idx + 1:len(s_product)]
        # удаляем лидирующие нули
        while not s_product.find('0'):
            s_product = s_product[1:len(s_product)]
        zero_idx = s_product.find('0', i)
    return i_max_product


def is_int(num):
    """
    проверяем число на целочисленность

    :param num:
    :return: True/False
    """
    try:
        int(num)
    except ValueError:
        return False
    return True


def pythagorean_triplet_reduce(sum_num):
    """
    9-я задача:
    Находит произведение тройки Пифагора, для которой сумма равна заданному числу

    :param sum_num:
    :return: triplet_product:
    """
    i = 2
    while True:
        # находим пару чисел [m_num, n_num] для генерации троек
        m_num = i
        n_num = (sum_num - 2 * m_num ** 2) / (2 * m_num)
        i += 1
        if (m_num > n_num) and (n_num > 0) and is_int(n_num):
            # вычисляем Пифагорову тройку
            a_side = m_num ** 2 - n_num ** 2
            b_side = 2 * m_num * n_num
            c_side = m_num ** 2 + n_num ** 2
            # проверяем тройку на соответствие исходной суммы
            if sum_num == sum([a_side, b_side, c_side]):
                break
    # вычисляем произведение
    triplet_product = a_side * b_side * c_side
    return triplet_product


def prime_nums_sum(max_num):
    """
    10-я задача:
    Находит сумму всех простых чисел меньше до указанного числа.

    :param max_num:
    :return: num_sum
    """
    start_sum = sum([2, 3, 5, 7, 11, 13])
    num_list = range(17, max_num)
    num_sum = sum([num for num in num_list if num % 2 != 0 if is_prime_num(num)])
    num_sum += start_sum
    return num_sum


def matrix_max_product(a_matrix):
    """
    11-я задача:
    Найти наибольшее произведение 4-х подряд идущих чисел в матрице
    направления: вверх, вниз, вправо, влево или по диагонали

    :param a_matrix:
    :return:
    """
    print a_matrix
    return 0
