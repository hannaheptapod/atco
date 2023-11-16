def main():
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    ans = solve(N, P)
    print(ans)


def solve(N, P):
    from itertools import combinations

    ans = 0
    for pi, pj in combinations(P, 2):
        xi, yi = pi
        xj, yj = pj

        dij = ((xi - xj) ** 2 + (yi - yj) ** 2) ** 0.5

        if dij > ans: ans = dij

    return ans


if __name__ == '__main__': main()
