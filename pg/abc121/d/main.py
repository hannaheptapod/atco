def main():
    A, B = map(int, input().split())

    ans = f(max(A-1, 0)) ^ f(B)
    print(ans)


def f(x): return x//2%2 ^ (x if not x%2 else 1)


if __name__ == '__main__': main()
