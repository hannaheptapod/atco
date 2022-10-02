def main():
    N, S = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = solve(N, S, arr)
    print(*ans, sep='\n')


def solve(N, S, arr):
    cards = [[h > t, abs(h-t)] for h, t in arr]
    mn = sum(arr[i][cards[i][0]] for i in range(N))

    if mn > S: return ['No']

    if mn == S: return make(cards[i][0] for i in range(N))

    sm = S-mn
    dp = [[False]*(sm+101) for _ in range(N+1)]
    dp[0][0] = True

    for i in range(N):
        for j in range(sm+1):
            if dp[i][j]:
                dp[i+1][j] = True
                dp[i+1][j+cards[i][1]] = True

    if not dp[N][sm]: return ['No']

    for i in range(N-1, -1, -1):
        if not dp[i][sm]:
            cards[i][0] = not cards[i][0]
            sm -= cards[i][1]

    return make(cards[i][0] for i in range(N))


def make(turns): return ['Yes', ''.join('T' if turn else 'H' for turn in turns)]


if __name__ == '__main__': main()
