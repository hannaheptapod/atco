def main():
    N, Q = map(int, input().split())
    A = sorted(map(int, input().split()))

    from bisect import bisect_left

    for _ in range(Q):
        x = int(input())
        idx = bisect_left(A, x)

        ans = N - idx
        print(ans)


if __name__ == '__main__': main()
