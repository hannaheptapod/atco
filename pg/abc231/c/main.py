from bisect import bisect_left


def main():
    N, Q = map(int, input().split())
    A = sorted(map(int, input().split()))

    for _ in range(Q):
        x = int(input())
        ans = N - bisect_left(A, x)
        print(ans)


if __name__ == '__main__': main()
