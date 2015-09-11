# coding=utf-8

import gc
import time
import euler

__author__ = 'sford'


def main():
    gc.enable()
    start = time.time()
    print euler.max_prime_factor_new(13195)

    print time.time() - start
    gc.collect()


if __name__ == '__main__':
    main()
