N = int(input())
w = [int(input()) for _ in range(N)]

ans = 1 + sum(w[i] < w[i+1] for i in range(N-1))
print(ans)
