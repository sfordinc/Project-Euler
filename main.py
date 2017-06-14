# coding=utf-8

import gc
import time
import euler

__author__ = 'sford'


def main():
    gc.enable()
    start = time.time()

    num = 12
    print euler.pythagorean_triplet_reduce(num)

    print time.time() - start
    gc.collect()


if __name__ == '__main__':
    main()
