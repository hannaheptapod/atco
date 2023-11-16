def main():
    H, W = map(int, input().split())
    G = [input() for _ in range(H)]

    ans = solve(H, W, G)
    print(*ans)


def solve(H, W, G):
    visited = [[False] * W for _ in range(H)]

    ni, nj = 0, 0
    while not visited[ni][nj]:
        visited[ni][nj] = True

        if G[ni][nj] == 'U' and ni > 0: ni -= 1
        elif G[ni][nj] == 'D' and ni < H - 1: ni += 1
        elif G[ni][nj] == 'L' and nj > 0: nj -= 1
        elif G[ni][nj] == 'R' and nj < W - 1: nj += 1
        else: return (ni+1, nj+1)

    return [-1]


if __name__ == '__main__': main()
