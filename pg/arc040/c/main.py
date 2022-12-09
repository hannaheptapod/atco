from bisect import bisect_left


def main():
    N = int(input())
    S = [input() for _ in range(N)]
    X = [[j for j, sij in enumerate(si) if sij == '.'] for si in S]

    ans = 0
    mx = N
    for xi in X:
        idx = bisect_left(xi, mx)
        if not idx:
            mx = N
            continue
        mx = xi[idx-1]
        ans += 1

    print(ans)


if __name__ == '__main__': main()
