n = int(input())
a = [int(input()) for _ in range(n)]
route = {1}
now = 1
while True:
    ai = a[now-1]
    if ai == 2:
        ans = len(route)
        break
    elif ai in route:
        ans = -1
        break
    else:
        route.add(ai)
        now = ai
print(ans)