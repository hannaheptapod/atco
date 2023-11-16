from atcoder.modint import ModContext, raw


def main():
    global MOD, A, B, C, D, E, F
    MOD = 998244353

    with ModContext(MOD):
        A, B, C, D, E, F = map(lambda x: raw(int(x)), input().split())

    ans = solve()

    print(ans)


def solve():
    with ModContext(MOD):
        res = A * B * C - D * E * F
        return res.val()


if __name__ == '__main__': main()
