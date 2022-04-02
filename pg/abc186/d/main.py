N = int(input())
A = sorted(map(int, input().split()))

ans = sum([A[i]*(2*i - N + 1) for i in range(N)])

print(ans)
