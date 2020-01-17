#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive
# recursive solution


def eating_cookies(amount, cache=None):
    if amount == 0:
        return 1
    print(amount)
    total = 0
    if amount - 3 >= 0:
        total += eating_cookies(amount-3)
    if amount - 2 >= 0:
        total += eating_cookies(amount-2)
    if amount - 1 >= 0:
        total += eating_cookies(amount-1)

    return total


if __name__ == "__main__":
    if len(sys.argv) > 1:
        num_cookies = int(sys.argv[1])
        print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(
            ways=eating_cookies(num_cookies), n=num_cookies))
    else:
        print('Usage: eating_cookies.py [num_cookies]')
