from bisect import bisect_left as bil

N = int(input())
a = list(map(int, input().split()))

a.sort()
s = set()

for ai in a:
    while ai % 2 == 0:
        ai >>= 1
    s.add(ai)

print(len(s))
