from collections import deque


def main():
    N, M = map(int, input().split())

    ans = solve(N, M)
    _ = [print(*a) for a in ans]


def solve(N, M):
    dp = [[-1]*N for _ in range(N)]
    dp[0][0] = 0

    dr = make_dr(N, M)

    deq = deque([(0, 0)])
    while deq:
        x, y = deq.popleft()
        dist = dp[x][y]

        for dx, dy in dr:
            nx, ny = x+dx, y+dy
            if 0 <= nx < N and 0 <= ny < N and dp[nx][ny] == -1:
                dp[nx][ny] = dist+1
                deq.append((nx, ny))

    return dp


def make_dr(N, M):
    dr = set()
    for i in range(N):
        if i**2 > M: break
        for j in range(i, N):
            if i**2 + j**2 > M: break
            if i**2 + j**2 == M:
                dr |= {(i, j), (j, i), (-i, j), (-j, i), (i, -j), (j, -i), (-i, -j), (-j, -i)}

    return dr


if __name__ == '__main__': main()
