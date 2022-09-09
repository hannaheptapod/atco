N = int(input())

ans = 0
i = 1
while i <= N:
    f = N//i
    nxt = N//f + 1

    ans += (nxt-i)*f
    i = nxt

print(ans)
