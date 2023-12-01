# Jesse and Cookies

#!/bin/python3

import math
import os
import random
import re
import sys

import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#


def cookies(k, A):
    # Write your code here
    ret = 0

    hq = heapq.heapify(A)
    while len(A) > 1 and A[0] < k:
        heapq.heappush(A, heapq.heappop(A) + 2 * heapq.heappop(A))
        ret += 1

    return ret if A[0] >= k else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
