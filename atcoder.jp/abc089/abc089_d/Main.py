def main():
    H, W, D = map(int, input().split())
    A = [list(map(lambda x: int(x)-1, input().split())) for _ in range(H)]
    Q = int(input())
    LR = [list(map(lambda x: int(x)-1, input().split())) for _ in range(Q)]

    X, Y = [[-1]*(H*W) for _ in range(2)]
    for i in range(H):
        for j in range(W):
            aij = A[i][j]
            X[aij], Y[aij] = i, j

    C = [[0]*-(-H*W//D) for _ in range(D)]
    for i in range(D):
        for j in range(i, H*W-D, D):
            C[i][j//D+1] = C[i][j//D] + abs(X[j+D]-X[j]) + abs(Y[j+D]-Y[j])

    for l, r in LR: print(C[l%D][r//D] - C[l%D][l//D])


if __name__ == '__main__': main()
