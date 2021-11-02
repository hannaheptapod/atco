n, m = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(m)]
start = 10**(n-1)
if n == 1: start -= 1
for i in range(start, 10**n):
    si = str(i)
    for sci in sc:
        if si[sci[0] - 1] != str(sci[1]):
            ans = -1
            break
    else:
        ans = si
        break
else: ans = -1
print(ans)