n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()
i, j, k, ctr = 0, 0, 0, 0
while(k < n):
    while(a[i] >= b[j]):
        j += 1
        if j == n:
            break
    if j == n:
        break
    while(b[j] >= c[k]):
        k += 1
        if k == n:
            break
    if k == n:
        break
    ctr += 1
    i += 1
    j += 1
    k += 1
print(ctr)