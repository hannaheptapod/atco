s = input()
n = len(s)
l = [str(int(si in 'AGCT')) for si in s]
t = ''.join(l)
ans = 0
for i in range(1, n+1):
    ones = '1' * i
    if ones in t: ans = i
print(ans)