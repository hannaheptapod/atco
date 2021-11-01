n, m = map(int, input().split())
ac = [False]*n
pe = [0]*n
an = pn = 0
for _ in range(m):
    p, s = input().split()
    p = int(p)-1
    if s == 'AC' and not ac[p]:
        ac[p] = True
        an += 1
        pn += pe[p]
    elif s == 'WA': pe[p] += 1
print(an, pn)