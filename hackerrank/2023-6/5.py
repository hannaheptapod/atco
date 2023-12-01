#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'kingRichardKnights' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER s
#  3. INTEGER_ARRAY knights
#


def kingRichardKnights(n, s, knights):
    # Write your code here
    return


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = int(input().strip())

    commands = []

    for _ in range(s):
        commands.append(list(map(int, input().rstrip().split())))

    knights_count = int(input().strip())

    knights = []

    for _ in range(knights_count):
        knights_item = int(input().strip())
        knights.append(knights_item)

    result = kingRichardKnights(n, s, knights)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()
