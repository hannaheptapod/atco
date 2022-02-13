from itertools import product
n = int(input())

ans = 0

for i in range(3, len(str(n))+1):
    for p in product('357', repeat=i):
        x = ''.join(p)
        if i == len(str(n)) and int(x) > n: break
        if all([j in x for j in '357']): ans += 1
    else: continue
    break

print(ans)