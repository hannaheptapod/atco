n = int(input())
h = list(map(int, input().split()))
for i in range(n-1, 0, -1):
    if h[i-1] > h[i] + 1:
        ans = 'No'
        break
    elif h[i-1] == h[i] + 1: h[i-1] -= 1
else: ans = 'Yes'
print(ans)