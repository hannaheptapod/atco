N, A, B = map(int, input().split())
S = [int(input()) for _ in range(N)]

if len(set(S)) == 1: print(-1)
else:
    P = B/(max(S) - min(S))
    Q = A - P*sum(S)/N
    print(P, Q)