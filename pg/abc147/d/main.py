MOD = 10**9+7


def main():
    N = int(input())
    A = list(map(int, input().split()))

    ans = 0
    for bit in range(60):  # 桁ごと
        msk = 1 << bit

        zero, one = 0, 0
        for ai in A:
            if ai & msk: one += 1
            else: zero += 1

        ans += msk * zero * one
        ans %= MOD

    print(ans)


if __name__ == '__main__': main()
