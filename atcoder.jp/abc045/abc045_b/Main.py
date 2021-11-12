d = {nomo:[input(), 0] for nomo in ('a', 'b', 'c')}
n = 'a'
while True:
    if d[n][1] == len(d[n][0]):
        ans = {'a':'A', 'b':'B', 'c':'C'}[n]
        break
    card = d[n][0][d[n][1]]
    d[n][1] += 1
    n = card
print(ans)