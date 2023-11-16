def main():
    N = int(input())
    P = list(map(int, input().split()))

    ans = max(0, max(P[1:])-P[0]+1) if N > 1 else 0
    print(ans)


if __name__ == '__main__': main()
