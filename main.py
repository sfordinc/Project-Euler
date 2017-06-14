# coding=utf-8

import gc
import time
import euler

__author__ = 'sford'


def main():
    gc.enable()
    start = time.time()
    num = 2000000
    print euler.prime_nums_sum(num)

    print time.time() - start
    gc.collect()


if __name__ == '__main__':
    main()
