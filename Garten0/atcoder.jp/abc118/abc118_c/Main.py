import numpy as np
n = int(input())
a = list(map(int, input().split()))
arr = np.array(a)
ans = np.gcd.reduce(arr)
print(ans)