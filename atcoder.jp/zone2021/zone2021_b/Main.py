n, d, h = map(int, input().split())
dh = [list(map(int,input().split())) for _ in range(n)]

lowh = [(-dh[i][0] * h + d * dh[i][1])/(d - dh[i][0]) for i in range(n)]

ans = max(lowh + [0])
print(float(ans))