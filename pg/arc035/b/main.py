from collections import Counter
import sys
sys.setrecursionlimit(10**9)

N = int(input())
T = sorted(int(input()) for _ in range(N))
MOD = 10**9 + 7


def factorial(i):
    if i == 1: return 1
    return i*factorial(i-1) % MOD


cnt = list(Counter(T).items())
ans, tot, num = 0, 0, 1
for t, c in cnt:
    ans += (2*tot + t*(c+1))*c//2
    tot += t*c
    num *= factorial(c)
    num %= MOD

print(ans)
print(num)
