from collections import Counter
from itertools import chain


def main():
    global M
    _, M = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = Counter(A)

    ans = solve(cnt)
    print(ans)


def solve(cnt):
    leng = len(cnt)
    if leng == M: return 0

    arr = sorted(cnt.items())
    for p, (k, _) in enumerate(arr):
        if (k+1)%M not in cnt: break

    sm = 0
    dp = [0]*leng
    for i in chain(range(p, -1, -1), range(leng-1, p, -1)):
        k, v = arr[i]
        prod = k*v
        sm += prod
        dp[i] = prod + (dp[(i+1)%leng] if (k+1)%M in cnt else 0)

    return sm - max(dp)


if __name__ == '__main__': main()
