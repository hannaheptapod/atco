from collections import defaultdict, deque


def main():
    N = int(input())
    lads = defaultdict(set, {1: set()})
    for _ in range(N):
        a, b = map(int, input().split())
        lads[a].add(b)
        lads[b].add(a)

    seen = set()
    deq = deque([1])
    while deq:
        u = deq.popleft()
        if u in seen: continue
        seen.add(u)

        for v in lads[u]: deq.append(v)

    ans = max(seen)
    print(ans)


if __name__ == '__main__': main()
