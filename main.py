# coding=utf-8
__author__ = 'sford'

import euler
import time


def main():
    start = time.time()

    num_count = 100
    print euler.sum_square_difference(num_count)

    print time.time() - start


if __name__ == '__main__':
    main()
