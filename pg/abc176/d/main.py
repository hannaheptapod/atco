

def main():
    global H, W, C, D, S
    H, W = map(int, input().split())
    C = tuple(map(lambda x: int(x)-1, input().split()))
    D = tuple(map(lambda x: int(x)-1, input().split()))
    S = [input() for _ in range(H)]

    ans = solve()
    print(ans)


def solve():
    INF = 1<<15
    dp = [[INF]*W for _ in range(H)]
    dp[C[0]][C[1]] = 0


if __name__ == '__main__': main()
