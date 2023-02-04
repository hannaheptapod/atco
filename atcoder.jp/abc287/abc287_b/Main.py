from collections import Counter

N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]

cnt_s = Counter(s[3:] for s in S)
st_t = set(T)

ans = 0
for k, v in cnt_s.items():
    if k in st_t: ans += v

print(ans)
