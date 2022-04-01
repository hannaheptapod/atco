n = int(input())
a = list(map(int, input().split()))

ans = (a[-1]-a[0])/(n-1)
print(ans)
