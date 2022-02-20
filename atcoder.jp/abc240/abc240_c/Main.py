N, X = map(int, input().split())
jump = [list(map(int, input().split())) for _ in range(N)]

pos = set([0])

for i in range(N):
    ai, bi = jump[i]
    tmp = set()

    for pi in pos:
        if pi+ai <= X: tmp.add(pi + ai)
        if pi+bi <= X: tmp.add(pi + bi)
    
    pos = tmp
    if pos: continue
    break

if X in pos: ans = 'Yes'
else: ans = 'No'

print(ans)