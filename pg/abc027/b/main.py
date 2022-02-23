N = int(input())
a = list(map(int, input().split()))

sm = sum(a)
if sm%N: ans = -1
else:
    ans, left = 0, sm

    for i in range(N-1, 0, -1):
        left -= a[i]
        if left != sm*i//N: ans += 1

print(ans)