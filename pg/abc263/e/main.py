"""
There are N squares called Square 1 though Square N. You start on Square 1.

Each of the squares from Square 1 through Square N−1 has a die on it.
The die on Square i is labeled with the integers from 0 through A_i, each occurring with equal probability. (Die rolls are independent of each other.)

Until you reach Square N, you will repeat rolling a die on the square you are on.
Here, if the die on Square x rolls the integer y, you go to Square x+y.

Find the expected value, modulo 998244353, of the number of times you roll a die.
"""

mod = 998244353

N = int(input())
A = list(map(int, input().split()))
