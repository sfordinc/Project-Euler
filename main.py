# coding=utf-8
__author__ = 'sford'

import euler
import time


def main():
    start = time.time()

    max_num = 20
    print euler.evenly_divisible_min_num(max_num)

    print time.time() - start


if __name__ == '__main__':
    main()
