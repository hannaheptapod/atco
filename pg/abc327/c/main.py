def main():
    A = [list(map(int, input().split())) for _ in range(9)]

    ans = solve(A)
    print(ans)


def solve(A):
    for i in range(9):
        S = set(aij for aij in A[i])
        if len(S) != 9: return 'No'

    for j in range(9):
        S = set(A[i][j] for i in range(9))
        if len(S) != 9: return 'No'

    for i in range(3):
        for j in range(3):
            S = set(A[3*i+k][3*j+l] for k in range(3) for l in range(3))
            if len(S) != 9: return 'No'

    return 'Yes'


if __name__ == '__main__': main()
