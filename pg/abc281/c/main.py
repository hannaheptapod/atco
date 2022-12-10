from bisect import bisect


def main():
    N, T = map(int, input().split())
    A = tuple(map(int, input().split()))

    cu = [0]*(N+1)
    for i, ai in enumerate(A): cu[i+1] = cu[i] + ai

    x = bisect(cu, T%cu[-1])
    y = T%cu[-1] - cu[x-1]

    print(x, y)


if __name__ == '__main__': main()
