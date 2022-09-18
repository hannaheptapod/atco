from collections import Counter


def main():
    _, M = map(int, input().split())
    cnt = Counter()
    for _ in range(M):
        a, b = map(int, input().split())
        cnt[a] += 1
        cnt[b] += 1

    ans = 'YES' if all([v % 2 == 0 for v in cnt.values()]) else 'NO'
    print(ans)


if __name__ == '__main__': main()
