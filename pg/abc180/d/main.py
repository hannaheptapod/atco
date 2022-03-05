X, Y, A, B = map(int, input().split())

exp, now = 0, X
while now*A < min(Y, now+B):
    exp += 1
    now *= A

ans = exp + (Y-now-1)//B

print(ans)
