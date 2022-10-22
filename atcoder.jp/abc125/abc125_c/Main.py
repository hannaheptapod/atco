from math import gcd


def main():
    N = int(input())
    A = list(map(int, input().split()))

    l, r = [0]*N, [0]*N
    l[0], r[N-1] = A[0], A[N-1]
    for i in range(1, N):
        l[i] = gcd(l[i-1], A[i])
        r[N-1-i] = gcd(r[N-i], A[N-1-i])

    ans = r[1]
    for i in range(1, N-1): ans = max(ans, gcd(l[i-1], r[i+1]))
    ans = max(ans, l[-2])
    print(ans)


if __name__ == '__main__': main()
