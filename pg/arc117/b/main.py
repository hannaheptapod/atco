MOD = 10**9 + 7

N = int(input())
A = [0] + sorted(set(map(int, input().split())))

diff = [A[i+1]-A[i] for i in range(len(A)-1)]
ans = 1
for di in diff: ans = ans*(di + 1) % MOD

print(ans)
