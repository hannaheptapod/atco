from bisect import bisect_right as bir, insort

MOD = 998244353


def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = [-1]*N
    arr = []

    for i, ai in enumerate(A):
        insort(arr, ai)

        if not i:
            ans[i] = ai
            continue

        ans[i] = (
            ans[i-1] * pow(i, 2, MOD) +
            (sum(max(ar, ai) for ar in arr)-ai) * 2 +
            ai
        ) * pow(i+1, -2, MOD) % MOD

    print(*ans, sep='\n')


if __name__ == '__main__': main()
