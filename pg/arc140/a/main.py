from collections import Counter

N, K = map(int, input().split())
S = input()

ans = N
for i in range(1, N):
    if N%i: continue

    if sum([max(Counter(S[j:N:i]).values()) for j in range(i)]) < N-K: continue
    ans = i
    break
print(ans)
