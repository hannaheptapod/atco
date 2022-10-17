def main():
    N = int(input())

    ans = f(N)
    print(ans)


def f(x): return x*f(x-1) if x else 1


if __name__ == '__main__': main()
