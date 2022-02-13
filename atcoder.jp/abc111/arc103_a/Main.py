from collections import Counter

n = int(input())
v = list(map(int, input().split()))

cnt = [Counter(v[i::2]).most_common(2)+[(0, 0)] for i in range(2)]

if cnt[0][0][0] != cnt[1][0][0]: ans = n - (cnt[0][0][1]+cnt[1][0][1])
else: ans = n - max(cnt[0][0][1]+cnt[1][1][1], cnt[0][1][1]+cnt[1][0][1])

print(ans)