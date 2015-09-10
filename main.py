# coding=utf-8

import gc
import time
import euler

__author__ = 'sford'


def main():
    gc.enable()
    start = time.time()
    print euler.prime_num(10)
    print euler.pythagorean_triplet(60)

    print time.time() - start
    gc.collect()


if __name__ == '__main__':
    main()
