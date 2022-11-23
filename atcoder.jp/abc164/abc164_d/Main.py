from collections import Counter


def main():
    S = input()

    ans = calc(S)
    print(ans)


def calc(S):
    N = len(S)

    cnt = Counter()
    cnt[0] = 1

    ret = 0
    tot, p = 0, 1
    for i in range(N-1, -1, -1):
        tot = (tot + int(S[i])*p) % 2019

        ret += cnt[tot]

        p = (p * 10) % 2019
        cnt[tot] += 1

    return ret


if __name__ == '__main__': main()
