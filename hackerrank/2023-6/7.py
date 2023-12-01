# Maximum Element

#!/bin/python3

import math
import os
import random
import re
import sys

from collections import deque, Counter

#
# Complete the 'getMax' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts STRING_ARRAY operations as parameter.
#


def getMax(operations):
    deq_stack, deq_max = deque(), deque()

    ret = []

    for op in operations:
        if op[0] == '1':
            x = int(op[2:])
            deq_stack.append(x)
            if not deq_max or deq_max[-1] <= x:
                deq_max.append(x)

        elif op == '2':
            x = deq_stack.pop()
            if x == deq_max[-1]:
                deq_max.pop()

        else:
            ret.append(deq_max[-1])

    return ret


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ops = []

    for _ in range(n):
        ops_item = input()
        ops.append(ops_item)

    res = getMax(ops)

    fptr.write('\n'.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
