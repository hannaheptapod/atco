from collections import Counter
N = int(input())

f = {}
for i in range(1, N+1):
    for j in range(int(i**0.5)+1, 0, -1):
        if not i%(j**2): break

    f[i] = j**2

cnt = Counter(i//f[i] for i in range(1, N+1))
ans = sum(ci**2 for ci in cnt.values())
print(ans)
