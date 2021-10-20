H, W, N = map(int, input().split())
A, B = [], []
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

row = {y:i+1 for i,y in enumerate(sorted(list(set(A))))}
col = {x:i+1 for i,x in enumerate(sorted(list(set(B))))}

_ = [print(row[a], col[b]) for a,b in zip(A,B)]