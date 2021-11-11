from itertools import combinations as com
n = int(input())
l = [0]*5
march = {'M':0, 'A':1, 'R':2, 'C':3, 'H':4}
for _ in range(n):
    s = input()[0]
    if s in march: l[march[s]] += 1
ans = 0
for ci in com(range(5), 3): ans += l[ci[0]]*l[ci[1]]*l[ci[2]]
print(ans)