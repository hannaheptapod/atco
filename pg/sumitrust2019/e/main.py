from collections import Counter


def main():
    global MOD, N, A
    MOD = 10**9 + 7
    N = int(input())
    A = list(map(int, input().split()))

    ans = calc()
    print(ans)


def calc():
    tmp = 1
    cnt = Counter([0]*3)
    for ai in A:
        tmp *= cnt[ai]
        tmp %= MOD
        cnt[ai] -= 1
        cnt[ai+1] += 1

    return tmp


if __name__ == '__main__': main()
