t = int(input())
for _ in range(t):
    l, m, n = map(int, input().split())
    ans = 0
    if m//2 <= n:
        ans += m//2
        n -= m//2
        if n//2 <= l:
            ans += n//2
            l -= n//2
            n %= 2
            ans += (2*l + 4*n)//10
        else:
            ans += l
    else:
        ans += n
        m -= 2*n
        if m <= l:
            ans += m//2
            l -= 2*(m//2)
            ans += l//5
        else:
            ans += l//2
    print(ans)