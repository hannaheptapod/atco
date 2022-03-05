N = int(input())
P = [list(map(int, input().split())) for _ in range(N)]

for cx in range(100 + 1):
    for cy in range(100 + 1):
        h = 1
        
        for pi in P:
            if pi[2]: h = pi[2] + abs(cx - pi[0]) + abs(cy - pi[1])
        
        if any([max(h - abs(pi[0]-cx) - abs(pi[1]-cy), 0) != pi[2] for pi in P]): continue
        
        ans = (cx, cy, h)
        break
    else: continue
    break

print(*ans)
