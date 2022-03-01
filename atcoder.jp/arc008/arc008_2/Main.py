from collections import Counter

N, M = map(int, input().split())
name = input()
kit = input()

C_n = Counter(name)
C_k = Counter(kit)

ans = 0
for ci in C_n.items():
    if ci[0] not in C_k:
        ans = -1
        break

    ans = max(ans, -int(-ci[1]//C_k[ci[0]]))

print(ans)