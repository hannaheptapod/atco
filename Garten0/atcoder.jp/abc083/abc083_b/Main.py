n, a, b = map(int, input().split())

def ss(x):
    xstr = '{:05}'.format(x)
    ss = sum(int(i) for i in xstr)
    return ss

ans = 0
for i in range(1, n + 1):
    ssi = ss(i)
    if ssi >= a and ssi <= b:
        ans += i
print(ans)