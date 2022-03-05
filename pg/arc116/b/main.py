N = int(input())
A = sorted(map(int, input().split()))
MOD = 998244353

ans = 0
for i in range(N, 0, -1):
    tmp = 0
