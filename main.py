# coding=utf-8
"""
base module of project euler
"""

import gc
import time
import euler

__author__ = 'sford'


def main():
    """
    execute one function of euler module
    :return: None
    """
    gc.enable()
    start = time.time()

    num = 600851475143
    print euler.max_prime_factor(num)

    print time.time() - start
    gc.collect()


if __name__ == '__main__':
    main()
