def main():
    N = int(input())
    S = [input() for _ in range(N)]

    from collections import Counter

    cnt = Counter()
    ans = []
    for s in S:
        ans += [s if cnt[s] == 0 else s + '(' + str(cnt[s]) + ')']
        cnt[s] += 1

    print(*ans, sep='\n')


if __name__ == '__main__': main()
