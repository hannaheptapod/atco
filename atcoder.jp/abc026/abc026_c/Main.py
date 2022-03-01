import sys
sys.setrecursionlimit(10**2)

N = int(input())
B = [-1] + [int(input())-1 for _ in range(N-1)]
INF = 10**9

G = [[] for _ in range(N)]
for i in range(1, N):
    G[B[i]].append(i)

def salary(x):
    if not G[x]: return 1

    mx, mn = 0, INF

    for j in G[x]:
        sj = salary(j)

        if sj > mx: mx = sj
        if sj < mn: mn = sj
    
    return mx + mn + 1

ans = salary(0)

print(ans)