from collections import Counter
from bisect import bisect_right


def main():
    global N, A
    N = int(input())
    A = list(map(int, input().split()))

    ans = solve()
    print(ans)


def solve():
    cnt = Counter(A)
    rem = sum(v-1 for v in cnt.values())

    arr = sorted(set(A))
    leng = len(arr)

    ok, ng = 0, N+1
    while abs(ng-ok) > 1:
        md = (ok+ng)//2

        idx = bisect_right(arr, md)
        if 2*(md - idx) <= leng - idx + rem: ok = md
        else: ng = md

    return ok


if __name__ == '__main__': main()
