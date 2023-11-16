def main():
    global T, tests
    T = int(input())
    tests = [int(input()) for _ in range(T)]

    for n in tests:
        ans = solve(n)
        print(*ans)

    return


def solve(n):
    for i in range(2, int(n**(1/3)) + 1):
        if n % i == 0:
            if n % (i**2) == 0: return i, n // (i**2)
            return int(pow(n // i, 0.5)), i
    return


if __name__ == '__main__': main()
