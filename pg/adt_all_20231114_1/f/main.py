from bisect import bisect_left


def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))

    for i in range(1, N+1):
        ans = A[bisect_left(A, i)] - i
        print(ans)


if __name__ == '__main__': main()
