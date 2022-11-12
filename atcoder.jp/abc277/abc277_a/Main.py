def main():
    N, X = map(int, input().split())
    P = list(map(int, input().split()))

    ans = P.index(X) + 1
    print(ans)


if __name__ == '__main__': main()
