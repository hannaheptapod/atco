from collections import Counter


def main():
    S = input()

    ans = solve(S)
    print(ans)


def solve(s):
    cnt = Counter(s)
    return (cnt['g']-cnt['p'])//2


if __name__ == '__main__': main()
