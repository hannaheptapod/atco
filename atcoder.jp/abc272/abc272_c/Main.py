def main():
    N = int(input())
    A = sorted(map(int, input().split()))
    O, E = [], []
    for ai in A:
        if ai % 2: O.append(ai)
        else: E.append(ai)

    ans = -1
    if len(O) > 1: ans = sum(O[-2:])
    if len(E) > 1: ans = max(ans, sum(E[-2:]))

    print(ans)


if __name__ == '__main__': main()
