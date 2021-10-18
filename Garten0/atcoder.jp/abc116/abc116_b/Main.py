def fn(n):
    if n%2 == 0:
        return n/2
    else:
        return 3*n + 1

s = int(input())
temp = s
set = set([s])
for i in range(1, 1000000):
    temp = fn(temp)
    if temp in set:
        ans = i+1
        break
    set.add(temp)
print(ans)