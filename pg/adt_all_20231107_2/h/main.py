MOD = 998244353


def main():
    T = int(input())

    for _ in range(T): solve()


def solve():
    N = int(input())
    S = input()

    S_left, S_right = S[:(N+1)//2], S[N//2:]

    ans = calc(S_left)
    if S_left[::-1] > S_right: ans -= 1
    ans %= MOD
    print(ans)


def calc(S):
    ans = 1
    for i, si in enumerate(S[::-1]):
        ans += pow(26, i, MOD) * (ord(si) - ord('A'))
        ans %= MOD

    return ans


if __name__ == '__main__': main()
