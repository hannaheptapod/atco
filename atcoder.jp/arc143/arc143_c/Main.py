N, X, Y = map(int, input().split())
A = list(map(lambda x: int(x)%(X+Y), input().split()))

mx = max(A)
if mx < X: ans = 'Second'
elif X <= Y and mx >= X: ans = 'First'
else:
    A = [ai-X if ai >= X else ai for ai in A]
    mx = max(A)
    if mx < X: ans = 'Second'
    elif X <= Y and mx >= X: ans = 'First'

print(ans)
