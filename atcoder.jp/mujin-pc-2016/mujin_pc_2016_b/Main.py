import math

l = list(map(int, input().split()))

mx = sum(l)
mn = max(0, 2*max(l) - mx)

ans = math.pi*(mx**2 - mn**2)
print(ans)
