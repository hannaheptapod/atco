from collections import defaultdict


def main():
    N, Q = map(int, input().split())

    follow = defaultdict(set)
    for _ in range(Q):
        t, a, b = map(int, input().split())

        if t == 1: follow[a].add(b)
        elif t == 2: follow[a] -= {b}
        else: print('Yes' if b in follow[a] and a in follow[b] else 'No')


if __name__ == '__main__': main()
