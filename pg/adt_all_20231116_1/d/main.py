def main():
    MOD = 998244353
    A, B, C, D, E, F = map(int, input().split())

    ans = A%MOD * B%MOD * C%MOD - D%MOD * E%MOD * F%MOD
    ans %= MOD
    print(ans)


if __name__ == '__main__': main()
