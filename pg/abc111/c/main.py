from collections import Counter

n = int(input())
v = list(map(int, input().split()))

c1, c2 = [Counter(v[i::2]).most_common(2)+[(0, 0)] for i in range(2)]

if c1[0][0] != c2[0][0]: ans = n - (c1[0][1]+c2[0][1])
else: ans = n - max(c1[0][1]+c2[1][1], c1[1][1]+c2[0][1])

print(ans)