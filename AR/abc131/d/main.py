n = int(input())
list = [_ for _ in range(n)]
for i in range(n):
    a, b = map(int, input().split())
    list[i] = [b, a]
list.sort()

time = 0

for ba in list:
    time += ba[1]
    if time <= ba[0]: continue
    else:
        ans = 'No'
        break
else: ans = 'Yes'

print(ans)