__author__ = 'sford'

import euler
import time


def main():
    start = time.time()

    num_size = 3
    print euler.max_palindrome(num_size)

    print time.time() - start


if __name__ == '__main__':
    main()
