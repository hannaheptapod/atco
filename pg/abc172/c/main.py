from bisect import bisect_right as bir

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

tot_a, tot_b = [0], [0]
for ai in A: tot_a.append(tot_a[-1] + ai)
for bi in B: tot_b.append(tot_b[-1] + bi)

ans = 0
for i in range(N+1):
    if tot_a[i] > K: break
    ans = max(ans, i + bir(tot_b, K - tot_a[i]) - 1)

print(ans)
