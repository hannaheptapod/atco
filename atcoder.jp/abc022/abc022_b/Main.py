from collections import Counter

N = int(input())
A = [int(input()) for _ in range(N)]
cnt = Counter(A)

ans = sum(ci - 1 for ci in cnt.values())
print(ans)
