def main():
    global N, X, A
    N, X = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    ans = dfs(0, 1)
    print(ans)


def dfs(depth, prod):
    if depth == N: return prod == X

    sm = 0
    for ai in A[depth][1:]: sm += dfs(depth + 1, prod * ai)

    return sm


if __name__ == '__main__': main()
