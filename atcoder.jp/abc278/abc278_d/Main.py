from collections import defaultdict


def main():
    N = int(input())
    A = list(map(int, input().split()))

    dic = defaultdict(int, {i+1: ai for i, ai in enumerate(A)})
    init = 0
    Q = int(input())
    for _ in range(Q):
        query = list(map(int, input().split()))

        if query[0] == 1: dic, init = defaultdict(int), query[1]
        elif query[0] == 2: dic[query[1]] += query[2]
        else: print(dic[query[1]] + init)


if __name__ == '__main__': main()
