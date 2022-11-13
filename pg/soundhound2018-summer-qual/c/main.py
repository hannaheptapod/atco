def main():
    N, M, D = map(int, input().split())

    ans = calc(N, M, D)
    print(ans)


def calc(N, M, D): return (N-D)*(2 if D else 1)/pow(N, 2) * (M-1)


if __name__ == '__main__': main()
