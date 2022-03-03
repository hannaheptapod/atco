C = int(input())
NML = [sorted(map(int, input().split())) for _ in range(C)]

s = [0]*3
for ni in NML:
    for j in range(3): s[j] = max(s[j], ni[j])

ans = s[0]*s[1]*s[2]

print(ans)
