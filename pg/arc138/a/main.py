N, K = map(int, input().split())
A = sorted([(ai, i) for ai, i in zip(map(int, input().split()), range(N))],
           key=lambda x: (x[0], -x[1]))

ans = N*2
j = -1
for ai, i in A:
    if i <= K-2: j = i
    elif j >= 0: ans = min(ans, 2*(j - i) - 1)

print(ans if ans < N*2 else -1)
