N, K = map(int, input().split())
S = input()

cnt = 0
for i in range(N-1):
    if S[i] == S[i+1]: cnt += 1

ans = min(N-1, cnt+2*K)
print(ans)