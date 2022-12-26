def main():
    N = int(input())
    P = [tuple(map(int, input().split())) for _ in range(N)]
    Z, W = [x+y for x, y in P], [x-y for x, y in P]

    ans = max(max(Z) - min(Z), max(W) - min(W))
    print(ans)


if __name__ == '__main__': main()
