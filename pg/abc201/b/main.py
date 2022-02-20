N = int(input())

monto = [['', 0] for _ in range(N)]
for i in range(N):
    s, t = input().split()
    monto[i] = [s, int(t)]

monto.sort(key=lambda x: x[1], reverse=True)

print(monto[1][0])