n = int(input())
a = list(map(int, input().split()))
size = sum(a)
a += a
ans = 'No'
l, r = 0, 1
leng  = a[0]
while l < n:
    if leng * 10 < size:
        leng += a[r]
        r += 1
    elif leng * 10 == size:
        ans = 'Yes'
        break
    else:
        leng -= a[l]
        l += 1
print(ans)