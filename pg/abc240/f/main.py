T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    C = [list(map(int, input().split())) for _ in range(N)]

    B = [C[0][0]]
    for i in range(1, N): B.append(B[i-1] + C[i-1][0]*(C[i-1][1]-1) + C[i][0])

    A = [[C[0][0], C[0][0]*C[0][1]*(C[0][1]+1)//2]]
    for i in range(1, N): A.append([A[-1][1]+B[i], A[-1][1]+B[i]*C[i][1]+C[i][0]*C[i][1]*(C[i][1]-1)//2])

    ans = max([max(ai) for ai in A])

    print(ans)