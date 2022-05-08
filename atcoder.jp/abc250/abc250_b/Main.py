N, A, B = map(int, input().split())

od, ev = '', ''
for i in range(N):
    if i%2:
        od += '.'*B
        ev += '#'*B
    else:
        od += '#'*B
        ev += '.'*B

X = [[od if i%2 else ev]*A for i in range(N)]

for i in range(N):
    for j in range(A):
        print(X[i][j])
