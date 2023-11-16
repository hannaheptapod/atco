def main():
    N = int(input())
    S = input()

    ans = solve(N, S)
    print(ans)


def solve(N, S):
    from collections import Counter

    cnt_s = Counter(S)

    ret = 0
    for i in range(10**N):
        t = str(i**2).zfill(N)
        if len(t) > N: break

        cnt_t = Counter(t)
        if cnt_s == cnt_t: ret += 1

    return ret


if __name__ == '__main__': main()
