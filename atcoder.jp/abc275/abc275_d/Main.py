from functools import lru_cache


def main():
    N = int(input())

    ans = f(N)
    print(ans)


@lru_cache
def f(x):
    if not x: return 1

    return f(x//2) + f(x//3)


if __name__ == '__main__': main()
