N, T = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(N)]

sm = sum([min(abi) for abi in AB])
if sm > T: ans = -1
else:
    diff = [abi[0]-abi[1] for abi in AB]
    diff.sort()
    
    ans = N
    for di in diff:
        sm += di
        if sm <= T: ans -= 1
        else: break

print(ans)
