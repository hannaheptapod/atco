#

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    ret = []

    for ci in s:
        if ci.isalpha():
            if ci.isupper():
                ret += chr((ord(ci) - ord('A') + k) % 26 + ord('A'))
            else:
                ret += chr((ord(ci) - ord('a') + k) % 26 + ord('a'))
        else:
            ret += ci

    return ''.join(ret)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()
