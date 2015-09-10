# coding=utf-8

import gc
import time
import euler

__author__ = 'sford'


def main():
    gc.enable()
    start = time.time()
    """
    i_list = (10, 50, 100, 500, 1000, 5000, 10000)
    for i in i_list:
        print euler.prime_num(i)
    """
    num = 10001
    print euler.prime_num(num)

    print time.time() - start
    gc.collect()


if __name__ == '__main__':
    main()
