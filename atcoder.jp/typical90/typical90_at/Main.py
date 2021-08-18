n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
am, bm, cm = [0]*46, [0]*46, [0]*46
for i in range(n):
    am[a[i]%46] += 1
    bm[b[i]%46] += 1
    cm[c[i]%46] += 1
ans = 0
for i in range(46):
    for j in range(46):
        k = 46 - i - j
        ans += am[i%46] * bm[j%46] * cm[k%46]
print(ans)
