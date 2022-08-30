from collections import Counter

N = int(input())
A = list(map(int, input().split()))

cnt = Counter(A)
for i in cnt.keys():
    if cnt[i] == 3: break

ans = i
print(ans)
