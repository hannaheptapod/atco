# Plus Minus

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    cnt = [0, 0, 0]

    for i in arr:
        if i > 0:
            cnt[0] += 1
        elif i < 0:
            cnt[1] += 1
        else:
            cnt[2] += 1

    _ = [print(f'{i/n:.6f}') for i in cnt]


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
