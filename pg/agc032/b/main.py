from itertools import combinations


def main():
    N = int(input())
    sm = N if N%2 else N+1

    ans = []
    for u, v in combinations(range(1, N + 1), 2):
        if u+v != sm: ans.append((u, v))

    print(len(ans))
    _ = [print(*a) for a in ans]


if __name__ == '__main__': main()
