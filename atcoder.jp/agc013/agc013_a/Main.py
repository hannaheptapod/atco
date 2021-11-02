n = int(input())
a = list(map(int, input().split()))
ans = 1
if n > 1:
    inc = int(a[1]-a[0]>0) - int(a[1]-a[0]<0)
    for i in range(n-1):
        if (inc == 1 and a[i+1]-a[i] < 0) or (inc == -1 and a[i+1]-a[i] > 0):
            ans += 1
            inc = 0
        elif inc == 0: inc = int(a[i+1]-a[i]>0) - int(a[i+1]-a[i]<0)
print(ans)