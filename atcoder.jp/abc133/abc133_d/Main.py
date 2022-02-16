n = int(input())
a = list(map(int, input().split()))

sm = sum(a)
a = a+a

ans = [sm-2*sum(a[1:n-1:2])]
for i in range(n-1): ans += [2*a[i] - ans[-1]]

print(*ans)