__author__ = 'sford'

import euler
import time


def main():
    start = time.time()

    # num_size = 3
    # print euler.max_palindrome(num_size)

    max_num = 17
    print euler.evenly_divisible_min_num(max_num)

    print time.time() - start


if __name__ == '__main__':
    main()
