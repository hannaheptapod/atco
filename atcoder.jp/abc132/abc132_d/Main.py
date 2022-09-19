MOD = 10**9 + 7


def main():
    N, K = map(int, input().split())

    for i in range(1, K+1):
        r, b = N - K - (i-1), K - i

        ans = hp(i, b)*hp(i+1, r) % MOD if r >= 0 else 0
        print(ans)


def hp(n, r):
    tmp = 1
    for i in range(1, r+1):
        tmp *= (n + r - i) * pow(i, -1, MOD)
        tmp %= MOD
    return tmp


if __name__ == '__main__': main()
