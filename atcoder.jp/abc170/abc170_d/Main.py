from collections import Counter, defaultdict


def main():
    N = int(input())
    A = sorted(map(int, input().split()))

    cnt = Counter(A)
    dic = defaultdict(lambda: True)

    for i in cnt:
        dic[i] &= cnt[i] == 1
        for j in range(2*i, A[-1]+1, i): dic[j] = False

    ans = sum([1 for a in A if dic[a]])
    print(ans)


if __name__ == '__main__': main()
