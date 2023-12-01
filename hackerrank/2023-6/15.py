def main():
    t = int(input())

    for _ in range(t):
        n, k = map(int, input().split())
        ans = solve(n, k)
        print(*ans)


def solve(n, k):
    if k == 0:
        return list(range(1, n+1))
    elif k == 1 and n % 2 == 0:
        return [i+1 if (i+1)%2==0 else i-1 for i in range(1, n+1)]
    elif n % (2*k) == 0:
        return [i+k if ((i-1)//k)%2==0 else i-k for i in range(1, n+1)]
    else:
        return [-1]


if __name__ == '__main__': main()
