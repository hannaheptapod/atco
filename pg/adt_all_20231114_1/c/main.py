def main():
    N = int(input())
    S = [input() for _ in range(N)]

    from collections import Counter
    cnt = Counter(S)

    ans = cnt.most_common()[0][0]
    print(ans)


if __name__ == '__main__': main()
