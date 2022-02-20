N = int(input())

lo, up = [], []

for i in range(1, int(N**0.5) + 1):
    if N%i == 0:
        lo.append(i)
        if i != N//i: up.append(N//i)

div = lo[1:] + up[::-1]

ans = sum([di - 1 for di in div if N//(di-1) == N%(di-1)])

print(ans)