N = int(input())
A = list(map(int, input().split()))

ans = N * sum([a**2 for a in A]) - (sum(A))**2
print(ans)