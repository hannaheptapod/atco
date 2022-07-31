N = int(input())
a = [-1] + list(map(int, input().split()))

s, t = 0, 0
for i in range(1, N+1):
    if a[i] == i: s += 1
    elif a[a[i]] == i: t += 1

ans = s*(s-1)//2 + t//2
print(ans)
