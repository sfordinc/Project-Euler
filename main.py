# coding=utf-8

import gc
import time
import euler

__author__ = 'sford'


def main():
    gc.enable()
    start = time.time()

    sum_num = 60
    print euler.pythagorean_triplet(sum_num)

    print time.time() - start
    gc.collect()


if __name__ == '__main__':
    main()
