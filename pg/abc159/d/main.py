def nc2(num): return num*(num-1) // 2
n = int(input())
a = list(map(int, input().split()))
l = [0]*(n+1)
ans= 0
for ai in a: l[ai] += 1
l[a[0]] -= 1
for li in l: ans += nc2(li)
print(ans)
for i in range(n-1):
    ans -= nc2(l[a[i]]) + nc2(l[a[i+1]])
    l[a[i]] += 1
    l[a[i+1]] -= 1
    ans += nc2(l[a[i]]) + nc2(l[a[i+1]])
    print(ans)