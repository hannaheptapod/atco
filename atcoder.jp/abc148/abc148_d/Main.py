n = int(input())
a = list(map(int, input().split()))
tmp = 0
for ai in a:
    if ai == tmp + 1: tmp += 1
if tmp > 0: ans = n - tmp
else: ans = -1
print(ans)