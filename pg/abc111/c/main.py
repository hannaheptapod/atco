n = int(input())
v = list(map(int, input().split()))

d = [{}, {}]

for i in range(n):
    if v[i] not in d[i%2]: d[i%2][v[i]] = 0
    d[i%2][v[i]] += 1

l = [[[0, 0]], [[0, 0]]]
for i in d[0].keys(): l[0] += [[d[0][i], i]]
for i in d[1].keys(): l[1] += [[d[1][i], i]]
l[0] = sorted(l[0], reverse=True)
l[1] = sorted(l[1], reverse=True)

if l[0][0][1] != l[1][0][1]: ans = n-(l[0][0][0] + l[1][0][0])
else: ans = n-max(l[0][0][0] + l[1][1][0], l[0][1][0], l[1][0][0])

print(ans)