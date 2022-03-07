from itertools import product

N, K = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(N)]

for v in product(*T):
    tmp = 0
    
    for vi in v: tmp ^= vi
    if tmp: continue
    
    ans = 'Found'
    break
else: ans = 'Nothing'

print(ans)
