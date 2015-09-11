# coding=utf-8

import gc
import time
import euler

__author__ = 'sford'


def main():
    gc.enable()
    start = time.time()
    print euler.is_prime_num(104743)

    print time.time() - start
    gc.collect()


if __name__ == '__main__':
    main()
